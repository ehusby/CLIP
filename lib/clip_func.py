from __future__ import print_function
import traceback

def display_error_message():
    print("--- ERROR ---")
    traceback.print_exc()
    print("-------------")

def wait_for_user_exit():
    print("\nPress [ENTER] to exit")
    try:
        input_bwc = raw_input
    except NameError:
        input_bwc = input
    _ = input_bwc()

def test_pyperclip_import():
    try:
        import pyperclip
    except ImportError:
        print("Required Python package 'pyperclip' not found.\nTry running the following command in Windows Command Prompt to install it:\n")
        print("pip install pyperclip")

def test_pyperclip_import_standalone():
    try:
        test_pyperclip_import()
    except:
        display_error_message()
        wait_for_user_exit()
