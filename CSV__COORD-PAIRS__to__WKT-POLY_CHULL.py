#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re
    from lib.chull import convex_hull

    coord_pair_lines = [re.sub(r",+", r",", re.sub(r"\s+", r",", line.strip())) for line in pyperclip.paste().strip().splitlines()]

    coord_pair_list = [[float(coord) for coord in line.split(',')] for line in coord_pair_lines]
    coord_pair_list = convex_hull(coord_pair_list)
    if coord_pair_list[-1] != coord_pair_list[0]:
        coord_pair_list.append(coord_pair_list[0])

    wkt = "POLYGON (({}))".format(
        ','.join([' '.join([str(coord) for coord in coord_pair]) for coord_pair in coord_pair_list])
    )
    pyperclip.copy(wkt)

except:
    base_func.display_error_message()
