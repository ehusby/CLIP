#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import re

    region = 'eu-central-1'

    s = pyperclip.paste()
    s = re.sub(
        r"^.*s3://([^/]+)/([^ ]+).*$",
        fr"https://{region}.console.aws.amazon.com/s3/object/\1?region={region}&bucketType=general&prefix=\2",
        s
    )
    s = re.sub(
        r"^.*s3://([^/]+)/([^ ]+).*$",
        fr"https://{region}.console.aws.amazon.com/s3/object/\1?region={region}&bucketType=general&prefix=\2",
        s
    )
    s = re.sub(
        r"(/[^/\.]+)$",
        r"\1/",
        s
    )
    s = re.sub(
        r"/$",
        r"/&showversions=false",
        s
    )
    s = re.sub(
        r"aws.amazon.com/s3/object/(.*/&showversions=false)",
        r"aws.amazon.com/s3/buckets/\1",
        s
    )
    pyperclip.copy(s)

except:
    base_func.display_error_message()
