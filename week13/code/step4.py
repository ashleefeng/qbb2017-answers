#! /usr/bin/env python

"""
Usage:
./step4.py ../week13_data/abundance_table_assigned.tab
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram

filename = sys.argv[1]
df = pd.read_csv(filename, sep = '\t', index_col = 0)

def plot_heatmap(df, title):
    fig = plt.figure(figsize=(25, 10))
    ax = fig.add_subplot(111)
    plt.pcolor(df)
    plt.title(title)
    plt.xticks(np.linspace(0.5, 17.5, num = 18))
    ax.set_xticklabels(df.columns, rotation=90)
    plt.yticks(np.linspace(0.5, 7.5, num=8), df.index)
    plt.xlabel("Sample")
    plt.ylabel("Predicted taxon")
    plt.savefig(title + '.png')
    plt.close

plot_heatmap(df, 'abundance2')

z = linkage(df)
idx = leaves_list(z)
df = df.iloc[idx]

plot_heatmap(df, "Sorted_abundance")