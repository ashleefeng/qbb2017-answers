#! /usr/bin/env python

"""
Usage: ./gap_inserter.py <nucleotide sequences file> <amino acid alignment file> > <output file name>
"""

import fasta
import sys
import itertools as it

nu_file = open(sys.argv[1])
aa_file = open(sys.argv[2])

nu_reader = fasta.FASTAReader(nu_file)
aa_reader = fasta.FASTAReader(aa_file)

for (nident, nseq), (aident, aseq) in it.izip(nu_reader, aa_reader):
    new_nseq = ''
    nid = 0
    for aa in aseq:
        if aa == '-':
            new_nseq += '---'
        else:
            new_nseq += nseq[nid: nid + 3]
        nid += 3
    print '>' + nident
    print new_nseq


