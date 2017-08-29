#!/usr/bin/env python

import sys

counter = 0.0
sum = 0.0

for line in sys.stdin:
    if list(line)[0] == "@":
        continue
    else:
        counter += 1
        entries = line.split("\t")
        sum += float(entries[4])

print sum/counter