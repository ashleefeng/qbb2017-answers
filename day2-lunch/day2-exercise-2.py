#!/usr/bin/env python

import sys

counter = 0

for line in sys.stdin:
    if list(line)[0] == "@":
        continue
    else:
        entries = line.split("\t")
        if "NM:i:0" in entries:
            counter += 1

print counter
