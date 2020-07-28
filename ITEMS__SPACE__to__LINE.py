import lib.pyperclip_test
import pyperclip

pyperclip.copy(pyperclip.paste().replace(' ', '\n'))
