#!/usr/bin/env python

import sys

for line in sys.stdin:
    if "DROME" in line:
        tokens = line.rstrip("\r\n").split()
        uniprotID = tokens[-2]
        flybaseID = tokens[-1]
        if "FB" not in flybaseID:
            continue
        print "%s\t%s" %(flybaseID, uniprotID)
    
        
    