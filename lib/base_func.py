
from __future__ import print_function
import traceback
import sys


class ClipSyntaxError(Exception):
    def __init__(self, msg=""):
        super(Exception, self).__init__(msg)

class ClipLookupError(Exception):
    def __init__(self, msg=""):
        super(Exception, self).__init__(msg)


def display_error_message():
    print("\n--- ERROR ---")
    traceback.print_exc()
    print("-------------")


def wait_for_user_exit():
    print("\nPress [ENTER] to exit", end='')
    try:
        input_bwc = raw_input
    except NameError:
        input_bwc = input
    _ = input_bwc()
    sys.exit(1)


def test_pyperclip_import():
    try:
        import pyperclip
    except ImportError:
        print("\nERROR: Required Python package 'pyperclip' not found.")
        print("Try running the following command to install it:\n\n`{}`".format(
            "pip install pyperclip"
        ))
        wait_for_user_exit()


def test_pyperclip_import_standalone():
    try:
        test_pyperclip_import()
    except Exception:
        display_error_message()
        wait_for_user_exit()
