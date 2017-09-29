#! /usr/bin/env python

"""
Usage: ./00-af_spectrum.py <vcf file> <output>
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt

file = open(sys.argv[1])
output = sys.argv[2]

afs = []

for line in file:
    
    if line[0] == '#':
        continue
    else:
        tokens = line.rstrip('\n').split('\t')
        info = tokens[7]
        info_tokens = info.split(';')
        af = info_tokens[3].split('=')[1]
        for value in af.split(','):
            afs.append(float(value))

plt.figure()
p = plt.hist(afs, bins = 20)
plt.xlabel('Allele frequency')
plt.ylabel('Count')
plt.title('Allele Spectrum')
plt.savefig(output)
plt.close()