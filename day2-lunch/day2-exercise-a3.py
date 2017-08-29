#!/usr/bin/env python

import sys

counter = 0
bad_counter = 0

for line in sys.stdin:
    if list(line)[0] == "@":
        continue
    raw = line.split("\t")[10]
    phred_sum = 0.0
    length = 0.0
    for c in raw:
        phred_sum += ord(c)
        length += 1
    average = phred_sum / length - 30
    if average > 30:
        counter += 1
    else:
        bad_counter += 1

print counter