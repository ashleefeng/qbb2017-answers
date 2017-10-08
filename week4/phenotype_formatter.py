#! /usr/bin/python

"""
Usage: ./phenotype_formatter.py BYxRM_PhenoData.txt > BYxRM_PhenoData_final.tsv

"""

import pandas as pd
import sys

file = open(sys.argv[1])

for line in file:
    tokens = line.rstrip('\n').split('\t')
    print '\t'.join(tokens[0].split('_')) + '\t' + '\t'.join(tokens[1:])

