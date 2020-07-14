import pyperclip_test
import pyperclip

pyperclip.copy(pyperclip.paste().replace('\\', '/').replace('V:', '/mnt'))
