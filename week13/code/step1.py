#! /usr/bin/env python

import sys

filename = sys.argv[1]
file = open(filename)

outfilename = filename.split('.')[0] + '.krona'
outfile = open(outfilename, 'w')

taxa2count = {}

# i = 0

for line in file:
    # i += 1
    
    tokens_by_space = line.rstrip('\n').split('\t')
    readID = tokens_by_space[0]
    taxa = tokens_by_space[1]
    
    if taxa in taxa2count:
        taxa2count[taxa] += 1
    else:
        taxa2count[taxa] = 1
    
    
    # print readID
    # print taxa
    
    # if i == 5:
    #     break
    
for taxa in taxa2count:
    
    count = taxa2count[taxa]
    taxa_tab = '\t'.join(taxa.split(';'))
    
    line = str(count) + '\t' + taxa_tab + '\n'
    outfile.write(line)

file.close()
outfile.close()

