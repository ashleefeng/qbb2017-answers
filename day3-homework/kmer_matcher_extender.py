#!/usr/bin/env python

"""
for each matched k-mer will extend on either end to find the longest exact match. 
For each target sequence, print the matches ordered from longest to shortest.
usage: kmer_matcher_extender.py kmer_matcher.out
"""

import sys

name2pos = {}

file = open(sys.argv[1])

for line in file:
        
    tokens = line.rstrip("\r\n").split("\t")
    name = tokens[0]
    target_pos = int(tokens[1])
    query_pos = int(tokens[2])
    seq = tokens[3]
    
    if name not in name2pos:
        name2pos[name] = [(target_pos, seq, query_pos)]
    else:
        name2pos[name].append((target_pos, seq, query_pos))

print "seq_name\tsequence\tlength"

for name, pos_list in name2pos.iteritems():
    
    matches = []
    pos_list.sort(key=lambda tup: tup[2])
    prev_query_pos = -2
    prev_target_pos = -2
    prev_match = ""
    
    for (target_pos, seq, query_pos) in pos_list:
        # print target_pos, seq, query_pos
        
        curr_match = seq
        
        if query_pos == prev_query_pos + 1 and target_pos == prev_target_pos + 1:
            # print "extending"
            curr_match = prev_match + curr_match[-1]
        
        elif prev_match:
            matches.append((prev_match, len(prev_match), target_pos))
        
        prev_query_pos = query_pos
        prev_target_pos = target_pos
        prev_match = curr_match
            
    
    matches.sort(key=lambda tup: -tup[1])
    
    for (match, length, pos) in matches:
        if length > 11:
            print "%s\t%s\t%d" %(name, match, length)