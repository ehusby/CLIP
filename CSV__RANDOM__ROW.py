#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import csv
    import random

    csv_fp = pyperclip.paste().strip('\'"')
    field_list = None
    rows_list = None

    with open(csv_fp, 'r') as csv_fo:
        reader = csv.DictReader(csv_fo)
        rows_list = [row for row in reader]
        field_list = reader.fieldnames

    random_row = random.choice(rows_list)
    for field in field_list:
        value = random_row[field]
        print("{}: {}".format(field, value))

except:
    base_func.display_error_message()
else:
    base_func.wait_for_user_exit()
