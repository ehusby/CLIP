#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

try:
    import re

    pyperclip.copy(re.sub(r"(\s)+", r"\1", pyperclip.paste()))

except:
    base_func.display_error_message()
