#!/usr/bin/env python

from lib import base_func
try:
    import sys

    print(f"Python executable location:\n\n{sys.executable}")

except:
    base_func.display_error_message()
else:
    base_func.wait_for_user_exit()
