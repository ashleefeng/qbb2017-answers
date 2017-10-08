#! /usr/bin/python

import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt

input_file = open(sys.argv[1])
output_filename = sys.argv[2]

df = pd.read_csv(input_file, sep = '\\s+')

ps = (-1) * np.log10(df['P'])

# print ps
plt.figure()
plt.scatter(range(1, 1 + len(ps)), ps, marker = '.', s = 5)
plt.xlabel('chromosome postion')
plt.ylabel('-log10(P)')
plt.title('Manhattan plot')
plt.savefig(output_filename)
plt.close()

