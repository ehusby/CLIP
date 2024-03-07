#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re
    import xml.etree.ElementTree as ET
    try:
        from StringIO import StringIO  # Python 2
    except ImportError:
        from io import StringIO  # Python 3

    coord_xml_tag_list = [
        'ULLON', 'ULLAT',
        'URLON', 'URLAT',
        'LRLON', 'LRLAT',
        'LLLON', 'LLLAT',
        'ULLON', 'ULLAT',
    ]

    text = pyperclip.paste()
    band_p_block = re.search(r"<BAND_P>.*?</BAND_P>", text, flags=re.DOTALL)
    if band_p_block is None:
        text = "<BAND_P>\n{}\n</BAND_P>".format(text)
    else:
        text = band_p_block.group()

    root = ET.parse(StringIO(text)).getroot()
    coord_list = [str(float(root.find(coord_xml_tag).text)) for coord_xml_tag in coord_xml_tag_list]
    coord_pair_list = zip(coord_list[::2], coord_list[1::2])

    wkt = "POLYGON (({}))".format(
        ','.join([' '.join(coord_pair) for coord_pair in coord_pair_list])
    )
    pyperclip.copy(wkt)

except:
    base_func.display_error_message()
