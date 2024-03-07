#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy(
f"""
read -r -d '' path_lines << EOM
{pyperclip.paste()}
EOM

echo "$path_lines" | xargs gdalbuildvrt test.vrt
"""
)
