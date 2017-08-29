#!/usr/bin/env python

import sys

counter = 0

for line in sys.stdin:
    if list(line)[0] == "@":
        continue
    chrom = line.split("\t")[2]
    start = int(line.split("\t")[3])
    if chrom == "2L" and start >= 10000 and start <= 20000:
        counter += 1

print counter