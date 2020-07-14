from __future__ import print_function
import sys
try:
    import pyperclip
except ImportError:
    print("Required Python package 'pyperclip' not found.\nTry running the following command in Windows Command Prompt to install it:\n")
    print("pip install pyperclip")
    print("\nPress [ENTER] to exit")
    try:
        input_bwc = raw_input
    except NameError:
        input_bwc = input
    _ = input_bwc()
    sys.exit(1)
