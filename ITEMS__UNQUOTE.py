#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import_standalone()
import pyperclip
try:
    import re

    clip_contents = pyperclip.paste()
    quote = clip_contents.lstrip()[0]
    if quote not in "`'\"":
        pass
    else:
        pyperclip.copy(re.sub(r"""{0}([^{0}]+?){0}""".format(quote), r"\g<1>", clip_contents))

except:
    base_func.display_error_message()
    base_func.wait_for_user_exit()
