from lib import base_func
base_func.test_pyperclip_import_standalone()
import pyperclip

pyperclip.copy("'{}'".format("', '".join(pyperclip.paste().splitlines())))
