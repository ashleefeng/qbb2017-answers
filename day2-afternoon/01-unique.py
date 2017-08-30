#!/usr/bin/env python

import sys
gene_name_counts = {}

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_name = fields[9]
    t_name = fields[5]
    if gene_name not in gene_name_counts:
        gene_name_counts[gene_name] = [t_name]
    else:
        gene_name_counts[gene_name].append(t_name)

for gnc, count in gene_name_counts.items():
    print gnc, count