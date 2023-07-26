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

    rows_list = None

    with StringIO(pyperclip.paste()) as fp:
        reader = csv.reader(fp, delimiter=',')
        rows_list = [row for row in reader]

    ncols = max([len(row) for row in rows_list])

    output_row_lines = []
    for i in range(ncols):
        output_row = [row[i] for row in rows_list]
        output_row_lines.append(','.join(output_row))

    pyperclip.copy('\n'.join(output_row_lines))

except:
    base_func.display_error_message()
