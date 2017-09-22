#! /usr/bin/env python

"""
Usage: <tsv alignment file> <output filename>

"""

import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

file = open(sys.argv[1])
output = sys.argv[2]

df = pd.read_csv(file, sep = '\t')

# df.sort_values('start1', inplace = True)

prev_contig_name = ''
x_start = 0
x_values = []
y_values = []

for row in df.iterrows():
    row1 = row[1]
    contig_name = row1['name2']
    contig_length = int(contig_name.split('_')[3])
    start1 = row1['start1']
    end1 = row1['end1']
    start2 = row1['start2']
    end2 = row1['end2']
    
    # print end1 - start1, end2-start2
    
    # assert((end1-start1) == (end2 - start2))
    if start1 < 1e5:
        x_values += range(x_start + start2 - 1, x_start + end2)
        y_values += range(start1 - 1, end2 - start2 + start1)
    
    if contig_name != prev_contig_name:
        x_start += contig_length
    prev_contig_name = contig_name
    
plt.figure()

plt.scatter(x_values, y_values, s = 0.1, alpha = 0.1)

plt.savefig(output + '.png')


