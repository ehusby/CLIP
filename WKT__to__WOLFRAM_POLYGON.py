#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    wkt = pyperclip.paste()
    wkt = wkt.replace('POLYGON', '').replace('MULTIPOLYGON', '').strip()

    pyperclip.copy(
        'Polygon[{}]'.format(
            re.sub(
                r"\.\d+", '',
                wkt.replace(' 0,', ',').replace(' 0)', ')').replace('((', '{{').replace('))', '}}').replace(',', '},{').replace(' ', ',')
            )
        )
    )

except:
    base_func.display_error_message()
