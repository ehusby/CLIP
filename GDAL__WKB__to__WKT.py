#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import binascii
    from osgeo import ogr

    wkt_lines = []
    for line in pyperclip.paste().splitlines():
        wkb_ascii = line.strip()
        if wkb_ascii == '':
            continue
        geom = ogr.CreateGeometryFromWkb(binascii.a2b_hex(wkb_ascii))
        wkt_lines.append(geom.ExportToWkt())

    pyperclip.copy('\n'.join(wkt_lines))

except:
    base_func.display_error_message()
