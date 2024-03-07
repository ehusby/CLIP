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

        idx_filename = header.index('filename')
        idx_s3location = header.index('s3_location')

        output_lines = []
        for row in reader:
            s3_filepath = f"{row[idx_s3location].rstrip('/')}/{row[idx_filename].lstrip('/')}"
            output_lines.append(s3_filepath)

        pyperclip.copy('\n'.join(output_lines))

except:
    base_func.display_error_message()
