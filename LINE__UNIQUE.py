#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    from collections import OrderedDict

    pyperclip.copy('\n'.join(OrderedDict.fromkeys(pyperclip.paste().splitlines())))

except:
    base_func.display_error_message()
