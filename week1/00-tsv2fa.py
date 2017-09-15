#! /usr/bin/env python

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep='\t', names=['gi', 'accver', 'seq'])

for index, gi, av, seq in df.itertuples():
    print ">gi: %d accver:%s" %(gi, av)
    # print seq
    new_seq = ''
    for i in seq:
        if i != '-':
            new_seq += i
    print new_seq

