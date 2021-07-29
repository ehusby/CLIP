#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy("st_intersects(wkb_geometry, st_geomfromewkt('{}'))".format(pyperclip.paste()))
