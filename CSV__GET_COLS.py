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

    with StringIO(pyperclip.paste()) as fp:
        reader = csv.reader(fp, delimiter=',')
        header = next(reader)

        print("-- First row field values --")
        nfields = len(header)
        idx_display_format = '{: >%d}' % len(str(nfields))
        for idx, field in enumerate(header):
            idx_display = idx_display_format.format(idx)
            print("{}: {}".format(idx_display, field))
        print('')

        use_first_row = ''
        while use_first_row not in ('y', 'n'):
            use_first_row = base_func.get_user_input("Include first row in output? (y/n): ")
            use_first_row = use_first_row.strip().lower()
        if use_first_row == 'y':
            fp.seek(0)

        field_col_idx_list = []
        while not field_col_idx_list:
            field_sel = base_func.get_user_input("Input field index (integer) or field name (string): ")
            field_sel_str_list = [n.strip() for n in field_sel.split(',')]

            valid_input = True
            for field_sel in field_sel_str_list:

                if field_sel.isdigit():
                    field_sel_n = int(field_sel)
                    if 0 <= field_sel_n < nfields:
                        field_col_idx_list.append(field_sel_n)
                    else:
                        print("\nInput integer ({}) is out of field index range [0, {}]\n".format(
                            field_sel_n, nfields-1
                        ))
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
                        print("\nInput string not found in header fields: '{}'".format(field_sel))
                        valid_input = False
                        break
                    else:
                        field_col_idx = header.index(field_sel)
                        field_col_idx_list.append(field_col_idx)

            if not valid_input:
                field_col_idx_list = []

        output_row_lines = []
        for row in reader:
            output_row_values = []
            for field_col_idx in field_col_idx_list:
                output_row_values.append(row[field_col_idx])
            output_row = ','.join(output_row_values)
            output_row_lines.append(output_row)

        pyperclip.copy('\n'.join(output_row_lines))

except:
    base_func.display_error_message()
