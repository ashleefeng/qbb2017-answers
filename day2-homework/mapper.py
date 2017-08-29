#!/usr/bin/env python

import sys

stfile = open(sys.argv[-1])
mapping = open(sys.argv[-2])
f2u = {}

no_match = "*"
skip_no_match = False
if len(sys.argv) > 3:
    if sys.argv[1] == "-s":
        skip_no_match = True

for line in mapping:
    tokens = line.rstrip("\r\n").split("\t")
    flybaseID = tokens[0]
    uniprotID = tokens[1]
    f2u[flybaseID] = uniprotID

for i, line in enumerate(stfile):
    tokens = line.rstrip("\r\n").split("\t")
    if i == 0:
        tokens.append("uniprot_ID")
        joined_tokens = "\t".join(tokens)
        print joined_tokens
    else:
        f_id = tokens[8]
        u_id = False
        if f_id in f2u.keys():
            u_id = f2u[f_id]
        elif not skip_no_match:
            u_id = no_match
        if u_id:
            tokens.append(u_id)
            joined_tokens = "\t".join(tokens)
            print joined_tokens
    
    
    


    
    
    