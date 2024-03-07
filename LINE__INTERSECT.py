#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip
try:
    import os

    outfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", "clip_intersect.txt")


    print("A ∩ B = C")

    input("Copy set A to clipboard then press [ENTER]")
    A = set(pyperclip.paste().strip().splitlines())

    input("Copy set B to clipboard then press [ENTER]")
    B = set(pyperclip.paste().strip().splitlines())

    print("C =")
    C = sorted(list(A.intersection(B)))
    for item in C:
        print(item)


    with open(outfile, 'w') as outfile_fp:
        for item in C:
            outfile_fp.write(item+'\n')
    pyperclip.copy('\n'.join(C))

    print("\nIntersect has been copied to clipboard and written to output textfile: " + outfile)

except:
    base_func.display_error_message()
else:
    base_func.wait_for_user_exit()
