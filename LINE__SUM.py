#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    pyperclip.copy(sum([float(x) for x in pyperclip.paste().splitlines()]))
except:
    base_func.display_error_message()
