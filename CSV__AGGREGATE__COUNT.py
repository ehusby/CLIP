#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import sys
    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO
    import csv
    import itertools
    from collections import OrderedDict

    def unique_ordered(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    with StringIO(pyperclip.paste()) as fp:
        reader = csv.reader(fp, delimiter=',')
        header = next(reader)

        print("-- First row field values --")
        nfields = len(header)
        idx_display_format = '{: >%d}' % len(str(nfields))
        for idx, field in enumerate(header):
            idx_display = idx_display_format.format(idx)
            print(f"{idx_display}: {field}")
        print('')

        input_str = ''
        while input_str not in ('y', 'n'):
            input_str = base_func.get_user_input("Is the first row a header with field names? (y/n): ")
            input_str = input_str.strip().lower()
        first_row_is_header = input_str == 'y'

        if not first_row_is_header:
            header = [str(n) for n in range(len(header))]
            fp.seek(0)

        base_field_col_idx = None
        while base_field_col_idx is None:
            field_sel = base_func.get_user_input("Input field index (integer) or field name (string) of column to base aggregation: ")
            field_sel_str_list = [n.strip() for n in field_sel.split(',')]

            valid_input = True

            if field_sel.isdigit():
                field_sel_n = int(field_sel)
                if 0 <= field_sel_n < nfields:
                    base_field_col_idx = field_sel_n
                else:
                    print(f"\nInput integer ({field_sel_n}) is out of field index range [0, {nfields-1}]\n")
                    valid_input = False
                    break

            else:
                # Allow string field name to be quoted,
                # in case the field name is somehow a string of numbers.
                for quote_char in ("'", '"', '`'):
                    if field_sel.startswith(quote_char) and field_sel.endswith(quote_char):
                        field_sel = field_sel.strip(quote_char)
                        break
                if field_sel not in header:
                    print(f"\nInput string not found in header fields: '{field_sel}'")
                    valid_input = False
                    break
                else:
                    field_col_idx = header.index(field_sel)
                    base_field_col_idx = field_sel_n

            if not valid_input:
                base_field_col_idx = None

        baseval_col_values = OrderedDict()
        header_idx_list = range(len(header))
        for row in reader:
            baseval = row[base_field_col_idx]
            col_list_values = baseval_col_values.setdefault(baseval, [[] for i in range(len(header))])
            for field_col_idx in header_idx_list:
                col_list_values[field_col_idx].append(row[field_col_idx])

        output_header = ','.join(list(itertools.chain(
            [
                header[base_field_col_idx],
                header[base_field_col_idx] + "_count",
            ],
            *[[fname + "_values",
               fname + "_uvalues",
               fname + "_count",
               fname + "_ucount"] for fname in
              [fname for idx, fname in enumerate(header) if idx != base_field_col_idx]]
        )))

        output_row_lines = [output_header]

        for baseval, col_list_values in baseval_col_values.items():
            output_row_values = [
                baseval,                                                # base fname
                str(sum([len(values) for values in col_list_values]))   # base + "_ucount"
            ] + [[] for i in range((len(header) - 2) * 4)]
            field_n = -1
            for field_col_idx in header_idx_list:
                if field_col_idx == base_field_col_idx:
                    continue
                field_n += 1
                col_values = col_list_values[field_col_idx]
                col_values_unique = unique_ordered(col_values)
                output_row_values[field_n * 4 + 1] = '"' + ','.join(col_values) + '"'           # fname + "_values"
                output_row_values[field_n * 4 + 2] = '"' + ','.join(col_values_unique) + '"'    # fname + "_uvalues"
                output_row_values[field_n * 4 + 3] = str(len(col_values))                       # fname + "_count"
                output_row_values[field_n * 4 + 4] = str(len(col_values_unique))                # fname + "_ucount"
            output_row = ','.join(output_row_values)
            output_row_lines.append(output_row)

        pyperclip.copy('\n'.join(output_row_lines))

except:
    base_func.display_error_message()
