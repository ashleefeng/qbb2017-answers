#!/usr/bin/env python

import sys

fwd = 0
rev = 0

for line in sys.stdin:
    if list(line)[0] == "@":
        continue
    else:
        flag = int(line.split("\t")[1])
        if (16 & flag) >> 4 == 0:
            fwd += 1
        else:
            rev += 1

print "forward alignments: ", fwd
print "reverse alignments: ", rev