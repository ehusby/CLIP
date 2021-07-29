#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    from lib.shared_func import geo_parse_coords, geo_get_epsg_code

    coords_list_lat_lon = geo_parse_coords(pyperclip.paste())
    # coords_epsg = geo_get_epsg_code()
    coords_epsg = 4326

    pyperclip.copy("st_intersects(wkb_geometry, st_setsrid(st_point({}, {}), {}))".format(
        *reversed(coords_list_lat_lon), coords_epsg
    ))

except:
    base_func.display_error_message()
