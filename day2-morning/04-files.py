#!/usr/bin/env python

import sys

# f = open("/Users/cmdb/data/genomes/BDGP6.fa")
if len(sys.argv) > 1:
    f = open(sys.argv[1])
    first_line = f.readline()
else:
    first_line = sys.stdin.readline() # enable pipe

print first_line