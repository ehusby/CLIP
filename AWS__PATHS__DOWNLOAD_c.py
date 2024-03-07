#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy(
f"""
read -r -d '' s3_lines << EOM
{pyperclip.paste()}
EOM

echo "$s3_lines" | while IFS= read -r s3_path; do
    aws_cmd cp "$s3_path" ./
done
"""
)
