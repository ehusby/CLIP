#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy(
f"""
read -r -d '' path_lines << EOM
{pyperclip.paste()}
EOM

echo "$path_lines" | while IFS= read -r path; do
    out_vrt=$(basename "$path")
    out_vrt="${{out_vrt%.*}}.vrt"
    gdalbuildvrt "$out_vrt" "$path"
done
"""
)
