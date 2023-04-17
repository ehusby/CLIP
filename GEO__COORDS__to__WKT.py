#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    coord_pair_lines = [re.sub(r"\s+", r"", line.strip()) for line in pyperclip.paste().strip().splitlines()]
    seen = set()
    seen_add = seen.add
    coord_pair_lines = [x for x in coord_pair_lines if not (x in seen or seen_add(x))]

    coord_pair_list = [line.split(',') for line in coord_pair_lines]
    if len(coord_pair_list) == 2:
        coord_a = coord_pair_list[0]
        coord_b = coord_pair_list[1]
        coord_pair_list = [
            coord_a,
            [coord_a[0], coord_b[1]],
            coord_b,
            [coord_b[0], coord_a[1]],
        ]
    coord_pair_list.append(coord_pair_list[0])

    wkt = "POLYGON (({}))".format(
        ','.join([' '.join(coord_pair) for coord_pair in coord_pair_list])
    )
    pyperclip.copy(wkt)

except:
    base_func.display_error_message()
