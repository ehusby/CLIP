#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re
    from lib.shared_func import distance_between_coordinates_meters

    per_n_meters = 1.0

    parsed_items = [float(v) for v in re.sub(r"[\s,]+", r",", pyperclip.paste()).strip(',').split(',')]
    if len(parsed_items) == 2:
        lat, lon = parsed_items
    else:
        lat, lon, per_n_meters = parsed_items

    dx = 0.002 / distance_between_coordinates_meters(lat, lon - 0.001, lat, lon + 0.001) * per_n_meters
    dy = 0.002 / distance_between_coordinates_meters(lat - 0.001, lon, lat + 0.001, lon) * per_n_meters

    pyperclip.copy("{:.10f},{:.10f}".format(dx, dy))

except:
    base_func.display_error_message()
