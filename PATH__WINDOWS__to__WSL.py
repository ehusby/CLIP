#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    pyperclip.copy(re.sub(r"^([\"\']*)\s*([A-Z]):", lambda m: f"{m.group(1)}/mnt/{m.group(2).lower()}", re.sub(r"\\+", "/", pyperclip.paste())))

except:
    base_func.display_error_message()
