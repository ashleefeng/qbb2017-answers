#! /usr/bin/env python

"""
Usage: ./00-contig.py <contig.fa>
"""

import fasta
import sys

def n50_finder(contig_lens):
    
    contig_lens.sort(reverse = True)
    
    l = sum(contig_lens)
    l2 = float(l)/2
    
    temp_sum = 0
    
    for length in contig_lens:
        
        temp_sum += length
        if temp_sum > l2:
            return length

file = open(sys.argv[1])

reader = fasta.FASTAReader(file)

contig_lens = []

for ident, seq in reader:
    
    contig_lens.append(len(seq))

print 'N50 is : ' + str(n50_finder(contig_lens))
print 'Min contig length: ' + str(min(contig_lens))
print 'Max contig length: ' + str(max(contig_lens))
print 'Average contig length: ' + str(float(sum(contig_lens))/len(contig_lens))

