#! /usr/bin/env python

import numpy as np
import pandas as pd


df = pd.read_csv('data/ctcf_peaks.tsv', '\t')
primers = pd.read_csv('data/Nora_Primers.bed', '\t')

data = np.load('Out_ctcf.npz')

enrichment = data['0.enrichment']
fwd = data['0.forward']
rev = data['0.reverse']

roi = df['#Chromosome'] == 'chrX'
Xctcf = df[roi]
ctcf_pos = Xctcf['Position']

# find forward and reverse primers that contain ctcf sites

fid = 0
rid = 0
fwd_ctcf = []
rev_ctcf = []

fstart = fwd[fid][0]
fend = fwd[fid][1]
rstart = rev[rid][0]
rend = rev[rid][1]
    
for i in ctcf_pos:
    
    # brute force
    
    # for fid in range(len(fwd)):
    #     fstart = fwd[fid][0]
    #     fend = fwd[fid][1]
    #     if i >= fstart and i <= fend:
    #         fwd_ctcf[fid] = 1
    #
    # for rid in range(len(rev)):
    #     rstart = rev[rid][0]
    #     rend = rev[rid][1]
    #     if i >= rstart and i <= rend:
    #         rev_ctcf[rid] = 1
   
    # faster alternative
    
    while i > fend:
        fid += 1
        if fid >= len(fwd):
            break
        fstart = fwd[fid][0]
        fend = fwd[fid][1]

    if i >= fstart and i <= fend:
        if len(fwd_ctcf) > 0:
            if fid != fwd_ctcf[-1]:
                fwd_ctcf.append(fid)
        else:
            fwd_ctcf.append(fid)

    while i > rend:
        rid += 1
        if rid >= len(rev):
            break
        rstart = rev[rid][0]
        rend = rev[rid][1]

    if i >= rstart and i <= rend:
        rev_ctcf.append(rid)
        
fwd_ctcf_pos = fwd[fwd_ctcf]
rev_ctcf_pos = rev[rev_ctcf]
enrich_ctcf = enrichment[fwd_ctcf][:, rev_ctcf]

# print fwd_ctcf
# print fwd_ctcf_pos
# print rev_ctcf_pos
# print enrich_ctcf

# for each fwd/rev, find the rev/fwd with strongest enrichment

fwd2rev = {}
rev2fwd = {}
fwd2revid = {}
rev2fwdid = {}

for fid in range(len(fwd_ctcf_pos)):
    rev_enrichment = enrich_ctcf[fid]
    max_rev = np.argmax(rev_enrichment)
    # fwd2rev[fwd_ctcf_pos[fid]] = rev_ctcf_pos[max_rev] # cannot hash ndarray
    fwd2revid[fid] = max_rev
    
for rid in range(len(rev_ctcf_pos)):
    fwd_enrichment = enrich_ctcf[:][rid]
    max_fwd = np.argmax(fwd_enrichment)
    # rev2fwd[rev_ctcf_pos[rid]] = fwd_ctcf_pos[max_fwd]
    rev2fwdid[rid] = max_fwd

print "Forward to reverse"
for i in fwd2revid:
    for j in range(len(primers['start'])):
        if (primers['start'][j] == fwd_ctcf_pos[i][0]) and (fwd_ctcf_pos[i][1] == primers['stop'][j]):
            fwd_name = primers['score'][j]
            break
    for j in range(len(primers['start'])):
        rev_id = fwd2revid[i]
        if (primers['start'][j] == rev_ctcf_pos[rev_id][0]) and (rev_ctcf_pos[rev_id][1] == primers['stop'][j]):
            rev_name = primers['score'][j]
            break
    print fwd_name, fwd_ctcf_pos[i], rev_name, rev_ctcf_pos[rev_id]
print "Reverse to forward"

for i in rev2fwdid:
    for j in range(len(primers['start'])):
        if (primers['start'][j] == rev_ctcf_pos[i][0]) and (rev_ctcf_pos[i][1] == primers['stop'][j]):
            rev_name = primers['score'][j]
            break
    for j in range(len(primers['start'])):
        fwd_id = rev2fwdid[i]
        if (primers['start'][j] == fwd_ctcf_pos[fwd_id][0]) and (primers['stop'][j] == fwd_ctcf_pos[fwd_id][1]):
            fwd_name = primers['score'][j]
            break
    print rev_name, rev_ctcf_pos[i], fwd_name, fwd_ctcf_pos[rev2fwdid[i]]