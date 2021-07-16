#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import_standalone()
import pyperclip
try:
    import os
    import collections

    outfile = os.path.expanduser('~/clip_duplicates.txt')


    item_list = pyperclip.paste().strip().splitlines()
    item_duplicates = [item for item, count in collections.Counter(item_list).items() if count > 1]

    for item in item_duplicates:
        print(item)


    with open(outfile, 'w') as outfile_fp:
        for item in item_duplicates:
            outfile_fp.write(item+'\n')
    pyperclip.copy('\n'.join(item_duplicates))

    print("\nDuplicate list has been copied to clipboard and written to output textfile: " + outfile)

except:
    base_func.display_error_message()
finally:
    base_func.wait_for_user_exit()
