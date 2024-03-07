#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import os

    outfname = None
    while not outfname:
        outfname = input("Enter filename for clipboard dump: ")

    outfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", outfname)

    with open(outfile, 'w') as outfile_fp:
        outfile_fp.write(pyperclip.paste())

except:
    base_func.display_error_message()
