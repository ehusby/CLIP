from lib import clip_func
clip_func.test_pyperclip_import_standalone()
import pyperclip

pyperclip.copy('\n'.join(pyperclip.paste().split()))
