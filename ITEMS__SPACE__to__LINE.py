import lib.pyperclip_test
import pyperclip

pyperclip.copy('\n'.join(pyperclip.paste().split()))
