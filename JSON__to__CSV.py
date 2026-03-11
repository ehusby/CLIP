#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import json
    from itertools import chain

    data = json.loads(pyperclip.paste())
    cols = sorted(set(chain(*[record.keys() for record in data])))
    csv_lines = [','.join([record[col] for col in cols]) for record in data]
    csv_lines.insert(0, ','.join(cols))
    pyperclip.copy('\n'.join(csv_lines))

except:
    base_func.display_error_message()
