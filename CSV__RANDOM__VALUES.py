#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import csv
    import random
    from collections import defaultdict

    csv_fp = pyperclip.paste().strip('\'"')
    field_list = None
    field_values_dict = defaultdict(list)

    with open(csv_fp, 'r') as csv_fo:
        reader = csv.DictReader(csv_fo)
        for row in reader:
            for field, value in row.items():
                if value.strip() != '':
                    field_values_dict[field].append(value)
        field_list = reader.fieldnames

    for field in field_list:
        random_value = random.choice(field_values_dict[field])
        print("{}: {}".format(field, random_value))

except:
    base_func.display_error_message()
else:
    base_func.wait_for_user_exit()
