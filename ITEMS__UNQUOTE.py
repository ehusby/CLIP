from lib import clip_func
clip_func.test_pyperclip_import_standalone()
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
    clip_func.display_error_message()
    clip_func.wait_for_user_exit()
