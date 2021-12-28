#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy('\n'.join([line for line in pyperclip.paste().splitlines() if (line != '' or line.strip() != '')]))
