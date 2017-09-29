#! /usr/bin/env python

"""
For each codon, determine the ratio of non-synonymous to synonymous changes
Produce a plot showing the ratio at each position in the sequence, and highlight sites under significant positive selection in red
u
Usage: ./03-selection.py <amino acid alignment guided nucleotide alignment> <amino acid alignment> > <output plot name>
"""

import sys
import matplotlib.pyplot as plt
import fasta
import itertools as it
import numpy as np
import statsmodels.stats.weightstats as st

# from http://colingorrie.github.io/outlier-detection.html#z-score-method
def outliers_z_score(ys):
    # threshold = 3
    threshold = 0.64

    # mean_y = np.mean(ys)
    mean_y = 0
    stdev_y = np.std(ys)
    z_scores = [(y - mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > threshold)


nu_file = open(sys.argv[1])
aa_file = open(sys.argv[2])
out_filename = sys.argv[3]

nu_reader = fasta.FASTAReader(nu_file)
aa_reader = fasta.FASTAReader(aa_file)

# mut = [[codon, aa, dn, ds], [codon, aa, dn, ds], ...]

index = 0
mut = []

for (nident, nseq), (aident, aseq) in it.izip(nu_reader, aa_reader):
    nid = 0
    # print aseq
    for aid in range(len(aseq)):
        aa = aseq[aid]
        codon = nseq[nid: nid + 3]
        
        if index == 0:
            mut.append([codon, aa, 0, 0])
            # print mut[aid]
            
        else:
            # print len(mut), aid
            refcodon, refaa, dn, ds = mut[aid]
            
            if codon != refcodon:
                if refaa == aa:
                    ds += 1
                else:
                    dn += 1
                    
            mut[aid] = [refcodon, refaa, dn, ds]
        
            # print mut[index]
            
        nid += 3
        
    index += 1

dnds = []
diff = []

for codon, aa, dn, ds in mut:
    diff.append(dn-ds)
    if ds == 0:
        # dnds.append([0, 0])
        dnds.append(0)
    else:
        # dnds.append([float(dn)/float(ds + dn), ds + dn])
        dnds.append(float(dn)/float(ds))
    
# print dnds

zscores = outliers_z_score(diff)

z_set = set()
for z in zscores[0]:
    # print z
    z_set.add(float(z))

dnds_log = np.log1p(dnds) - np.log(1 + 1)
dnds_log_z = []

zscores_list = []
for i in range(len(dnds_log)):
    if i in z_set:
        d = float(dnds_log[i])
        if d > 0:
            dnds_log_z.append(d)
            zscores_list.append(i)

plt.figure()

plt.bar(range(1, len(dnds) + 1), dnds_log, color = 'blue')
# plt.hold(True)
zscores1p = list([x+1 for x in zscores_list])
# print zscores1p
# print dnds_log_z
plt.bar(zscores1p, dnds_log_z, color = 'red')


plt.xlabel('amino acid position')
plt.ylabel('log(dN/dS)')

plt.savefig(out_filename + '.png')
plt.close()
