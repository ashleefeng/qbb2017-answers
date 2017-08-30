#!/usr/bin/env python

import sys

f = open(sys.argv[1])

# while True:
#     the_line = f.readline().rstrip("\r\n")
#     if not the_line:
#         break
#     print the_line

my_iter = iter(f)
while True:
    the_line = my_iter.next()
    print the_line