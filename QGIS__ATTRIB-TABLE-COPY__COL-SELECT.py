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
        reader = csv.reader(fp, delimiter='\t')
        header = next(reader)

        print("-- Attribute table fields --")
        nfields = len(header)
        idx_display_format = '{: >%d}' % len(str(nfields))
        for idx, field in enumerate(header):
            idx_display = idx_display_format.format(idx)
            print("{}: {}".format(idx_display, field))
        print('')

        field_col_idx = None
        while field_col_idx is None:
            field_sel = base_func.get_user_input("Input field index (integer) or field name (string): ")

            if field_sel.isdigit():
                field_sel_int = int(field_sel)
                if 0 <= field_sel_int < nfields:
                    field_col_idx = int(field_sel)
                else:
                    print("\nInput integer ({}) is out of field index range [0, {}]\n".format(
                        field_sel_int, nfields-1
                    ))
            else:
                # Allow string field name to be quoted,
                # in case the field name is somehow a string of numbers.
                for quote_char in ("'", '"', '`'):
                    if field_sel.startswith(quote_char) and field_sel.endswith(quote_char):
                        field_sel = field_sel.strip(quote_char)
                        break
                if field_sel not in header:
                    print("\nInput string not found in header fields: '{}'".format(field_sel))
                else:
                    field_col_idx = header.index(field_sel)

        field_row_values = []
        for row in reader:
            field_row_values.append(row[field_col_idx])

        pyperclip.copy('\n'.join(field_row_values))

except:
    base_func.display_error_message()
