#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    clip_contents = pyperclip.paste()
    quote = clip_contents.lstrip()[0]
    if quote not in "`'\"":
        pass
    else:
        pyperclip.copy(re.sub(r"""{0}+([^{0}]+?){0}+""".format(quote), r"\1", clip_contents))

except:
    base_func.display_error_message()
