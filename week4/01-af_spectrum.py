#! /usr/bin/env python

"""
Usage: ./01-af_spectrum.py <vcf file> <output>
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

file = open(sys.argv[1])
output = sys.argv[2]

afs = []
quals = []

for line in file:
    
    if line[0] == '#':
        continue
    else:
        tokens = line.rstrip('\n').split('\t')
        
        qual = float(tokens[5])
        quals.append(qual)
        
        info = tokens[7]
        # info_tokens = info.split(';')
        af = info.split('=')[1]
        for value in af.split(','):
            afs.append(float(value))

plt.figure()
p = plt.hist(afs, bins = 100)
plt.xlabel('Allele frequency')
plt.ylabel('Count')
plt.title('Allele Frequency Spectrum')
plt.savefig(output)
plt.close()

file.close()