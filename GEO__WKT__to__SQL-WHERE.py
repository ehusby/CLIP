#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    from lib.shared_func import geo_get_epsg_code

    geom_wkt = pyperclip.paste()
    geom_epsg = geo_get_epsg_code()

    pyperclip.copy(f"st_intersects(wkb_geometry, st_geomfromtext('{geom_wkt}', {geom_epsg}))")

except:
    base_func.display_error_message()
