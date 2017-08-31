#!/usr/bin/env python

"""
Usage: ./advanced.py <samples.csv> <ctab_dir> <replicates.csv> <gene_name>
plot timecourse mRNA level of specified gene for females and males
"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

gene = sys.argv[4]

df_samples = pd.read_csv(sys.argv[1])
soif = df_samples["sex"] == "female"
soim = df_samples["sex"] == "male"

df_samples2 = pd.read_csv(sys.argv[3])
soif2 = df_samples2["sex"] == "female"
soim2 = df_samples2["sex"] == "male"

fpkmsf = []
fpkmsm = []
fpkmsf2 = []
fpkmsm2 = []

df_gene = pd.DataFrame()

for sample in df_samples["sample"][soif]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep='\t')
    roi = df["gene_name"] == gene
    fpkmsf.append(df[roi]["FPKM"].mean())

for sample in df_samples["sample"][soim]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep='\t')
    roi = df["gene_name"] == gene
    fpkmsm.append(df[roi]["FPKM"].mean())
    
for sample in df_samples2["sample"][soif2]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep='\t')
    roi = df["gene_name"] == gene
    fpkmsf2.append(df[roi]["FPKM"].mean())

for sample in df_samples2["sample"][soim2]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep='\t')
    roi = df["gene_name"] == gene
    fpkmsm2.append(df[roi]["FPKM"].mean())


plt.figure()
plt.title(gene)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")

fplot, = plt.plot(fpkmsf, '^-', color='r')
mplot, = plt.plot(fpkmsm, 'o-', color='c')
fplot2, = plt.plot(range(4, 8), fpkmsf2, '^-', color='m')
mplot2, = plt.plot(range(4, 8), fpkmsm2, 'o-', color='blue')
plt.xticks(range(8),["10", "11", "12", "13", "14A", "14B", "14C", "14D"])


plt.legend([fplot, fplot2, mplot, mplot2], ["female", "female replicate", "male", "male replicate"], loc=0)
plt.savefig(gene + ".png")
plt.close()