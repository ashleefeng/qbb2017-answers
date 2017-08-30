#!/usr/bin/env python

import sys

sum_len = 0.0
counter = 0

for line in sys.stdin:
    length = int(line.rstrip("\r\n"))
    sum_len += length
    counter += 1

print sum_len / counter