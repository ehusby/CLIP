import lib.pyperclip_test
import pyperclip
import os

outfile = os.path.expanduser('~/clip_difference.txt')


print("A - B = C")

input("Copy set A to clipboard then press [ENTER]")
A = set(pyperclip.paste().strip().splitlines())

input("Copy set B to clipboard then press [ENTER]")
B = set(pyperclip.paste().strip().splitlines())

print("C =")
C = sorted(list(A.difference(B)))
for item in C:
    print(item)


with open(outfile, 'w') as outfile_fp:
    for item in C:
        outfile_fp.write(item+'\n')
pyperclip.copy('\n'.join(C))

print("\nDifference has been copied to clipboard and written to output textfile: " + outfile)
input("Press [ENTER] to exit")
