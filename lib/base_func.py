
from __future__ import print_function
import traceback
import sys


class ClipInputError(Exception):
    def __init__(self, msg=""):
        super(Exception, self).__init__(msg)

class ClipLookupError(Exception):
    def __init__(self, msg=""):
        super(Exception, self).__init__(msg)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_user_input(prompt):
    try:
        input_bwc = raw_input
    except NameError:
        input_bwc = input
    return input_bwc(prompt)


def wait_for_user_exit(exit_code=0):
    get_user_input("\nPress [ENTER] to exit")
    sys.exit(exit_code)


def display_error_message(msg=None, exit_after=True):
    eprint("\n--- ERROR ---")
    if msg is not None:
        eprint(msg)
    else:
        traceback.print_exc()
    eprint("-------------")
    if exit_after:
        wait_for_user_exit(1)


def test_pyperclip_import():
    try:
        import pyperclip
    except ImportError:
        display_error_message('\n'.join([
            "Required Python package 'pyperclip' not found.",
            "Try running the following command to install it:",
            "   pip install pyperclip",
        ]))
    except Exception:
        display_error_message()
