import pyperclip_test
import pyperclip

pyperclip.copy("--cid "+" --cid ".join(pyperclip.paste().splitlines()))
