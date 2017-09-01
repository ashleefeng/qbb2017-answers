#!/usr/bin/env python

"""
usage: ./promoter_finder.py <ctab file> <output filename>
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t')
output = []

for index, row in df.iterrows():

    row_out = {}
    row_out["chromosome"] = row["chr"]
    row_out["t_name"] = row["t_name"]
    row_out["FPKM"] = row["FPKM"] 
    if row["strand"] == "+":
        if row["start"] - 500 < 0:
            row_out["start"] = 0
        else:
            row_out["start"] = row["start"] - 500
        row_out["end"] = row["start"] + 500
    elif row["strand"] == "-":
        if row["end"] - 500 < 0:
            row_out["start"] = 0
        else:
            row_out["start"] = row["end"] - 500
        row_out["end"] = row["end"] + 500

    output.append(row_out)

df_out = pd.DataFrame(output)
df_out.to_csv(sys.argv[2] + ".bed", sep = '\t', index=False, header=False, columns = ["chromosome", "start", "end", "t_name", "FPKM"])