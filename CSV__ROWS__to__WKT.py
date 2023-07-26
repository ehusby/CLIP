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

        coord_idx_dict = {
            'X1': None,
            'X2': None,
            'Y1': None,
            'Y2': None,
        }

        for coord_name in sorted(list(coord_idx_dict.keys())):
            while True:
                coord_idx = base_func.get_user_input("{} coordinate field index: ".format(coord_name)).strip()
                if coord_idx.isdigit():
                    coord_idx = int(coord_idx)
                    if 0 <= coord_idx <= nfields:
                        if coord_idx in list(coord_idx_dict.values()):
                            print("\nInput integer ({}) was already selected for other coordinate field index\n".format(
                                coord_idx
                            ))
                        else:
                            coord_idx_dict[coord_name] = coord_idx
                            break
                    else:
                        print("\nInput integer ({}) is out of field index range [0, {}]\n".format(
                            coord_idx, nfields-1
                        ))

        output_row_lines = []
        for row in reader:
            coord_pair_list = [
                (row[coord_idx_dict['X1']], row[coord_idx_dict['Y1']]),
                (row[coord_idx_dict['X1']], row[coord_idx_dict['Y2']]),
                (row[coord_idx_dict['X2']], row[coord_idx_dict['Y2']]),
                (row[coord_idx_dict['X2']], row[coord_idx_dict['Y1']]),
                (row[coord_idx_dict['X1']], row[coord_idx_dict['Y1']]),
            ]
            wkt = "POLYGON (({}))".format(
                ','.join([' '.join(coord_pair) for coord_pair in coord_pair_list])
            )
            output_row_lines.append(wkt)

        pyperclip.copy('\n'.join(output_row_lines))

except:
    base_func.display_error_message()
