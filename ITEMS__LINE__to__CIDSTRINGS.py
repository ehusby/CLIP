from lib import base_func
base_func.test_pyperclip_import_standalone()
import pyperclip

pyperclip.copy("--cid "+" --cid ".join(pyperclip.paste().splitlines()))
