#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    pyperclip.copy('; '.join(
        re.sub(r"export ([^\s]+)=\"(.+)\"", r"\1=\2", pyperclip.paste()).splitlines()
    ))

except:
    base_func.display_error_message()
