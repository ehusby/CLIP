#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    pyperclip.copy(re.sub(r"\\+", "/", pyperclip.paste()).replace('/ad.umn.edu/geo', 'V:').replace('V:', '/mnt'))

except:
    base_func.display_error_message()
