#! /usr/bin/env python

"""
Usage: ./02-translation_filter.py <output from transeq 6-frame translation> > <output filename>
"""

import fasta
import sys

aa_file = open(sys.argv[1])

aa_reader = fasta.FASTAReader(aa_file)

for ident, seq in aa_reader:
    seq = seq.rstrip('*')
    wrong_frame = False
    # if seq[0] != 'M':
    #     wrong_frame = True
    #     continue
    for char in seq:
        if char == '*':
            wrong_frame = True
            break
    if not wrong_frame:
        print '>' + ident
        print seq