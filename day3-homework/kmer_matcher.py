#!/usr/bin/env python

"""
finds matching k-mers between a single query sequence and a database of targets
usage: kmer_matcher.py <target.fa> <query.fa> <k>
"""

import sys
import fasta

assert len(sys.argv) == 4

target_file = open(sys.argv[1])
query_file = open(sys.argv[2])
k = int(sys.argv[3])

target_iterator = fasta.FASTAReader(target_file)

# get query string

line = query_file.readline()
assert line.startswith (">")
sequences = []

while True:
    line = query_file.readline().rstrip("\r\n")
    if line == "":
        break
    else:
        sequences.append(line)

query_sequence = "".join(sequences).upper()

# build index for target: {kmer -> (sequence_name, start_position)}
kmer2target = {}

for ident, target_sequence in target_iterator:
    target_sequence = target_sequence.upper()
    for i in range(0, len(target_sequence) - k):
        kmer = target_sequence[i: i + k]
        if kmer not in kmer2target:
            kmer2target[kmer] = [(ident, i)]
        else:
            kmer2target[kmer].append((ident, i))

target_kmers = kmer2target.keys()

# go through query sequence and look up target kmers

for i in range(0, len(query_sequence) - k):
    query_kmer = query_sequence[i:i + k]
    if query_kmer in kmer2target:
        matches = kmer2target[query_kmer]
        for j in range(len(matches)):
            (target_name, target_start_pos) = matches[j]
            print "%s\t%d\t%d\t%s" %(target_name, target_start_pos, i, query_kmer)

target_file.close()
query_file.close()


