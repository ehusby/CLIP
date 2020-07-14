import pyperclip_test
import pyperclip

pyperclip.copy("'"+"', '".join(pyperclip.paste().splitlines())+"'")
