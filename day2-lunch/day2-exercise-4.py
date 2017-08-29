#!/usr/bin/env python

import sys

counter = 0

for line in sys.stdin:
    if counter == 10:
        break
    if list(line)[0] == "@":
        continue
    else:
        counter += 1
        entries = line.split("\t")
        print entries[2]