#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy(pyperclip.paste().replace(r'\\ad.umn.edu\geo', 'V:').replace('\\', '/').replace('V:', '/mnt').replace('U:', '/mnt'))
