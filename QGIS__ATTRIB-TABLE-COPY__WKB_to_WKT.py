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

    import binascii
    from osgeo import ogr

    with StringIO(pyperclip.paste()) as fp:
        reader = csv.reader(fp, delimiter=',')
        header = next(reader)

        print("-- Attribute table fields --")
        nfields = len(header)
        idx_display_format = '{: >%d}' % len(str(nfields))
        for idx, field in enumerate(header):
            idx_display = idx_display_format.format(idx)
            print(f"{idx_display}: {field}")
        print('')

        field_col_idx_list = []
        while not field_col_idx_list:
            field_sel = base_func.get_user_input("Input WKB field index (integer) or field name (string): ")
            field_sel_str_list = [n.strip() for n in field_sel.split(',')]

            valid_input = True
            for field_sel in field_sel_str_list:

                if field_sel.isdigit():
                    field_sel_n = int(field_sel)
                    if 0 <= field_sel_n < nfields:
                        field_col_idx_list.append(field_sel_n)
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
                        field_col_idx_list.append(field_col_idx)

            if not valid_input:
                field_col_idx_list = []

        output_row_lines = []
        for row in reader:
            output_row_values = []
            for field_col_idx, value in enumerate(row):
                if field_col_idx in field_col_idx_list:
                    output_row_values.append(
                        ogr.CreateGeometryFromWkb(binascii.a2b_hex(value)).ExportToWkt()
                    )
                else:
                    output_row_values.append(value)
            output_row = ','.join(output_row_values)
            output_row_lines.append(output_row)

        pyperclip.copy('\n'.join(output_row_lines))

except:
    base_func.display_error_message()
