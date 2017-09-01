#!/usr/bin/env python

"""
usage: ./regression.py <t_data.ctab> <.tab file 1> <.tab file 2>...
"""

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


df_exp = pd.read_csv(sys.argv[1], sep='\t')
marks = []

for arg in sys.argv[2:]:

    df_mark = pd.read_csv(arg, sep='\t', header=None, names = ["name", "size", "covered", "sum", "mean0", "mean"])
    marks.append(df_mark["mean"])

marks = pd.DataFrame(marks, index = sys.argv[2:])
marks = marks.T

exp = df_exp["FPKM"]

mod = sm.OLS(exp.T, marks)
marks = sm.add_constant(marks) # not sure why
res = mod.fit()

print(res.summary())
print res.bse

plt.figure()

plt.plot(marks, exp, '.')
# for arg in sys.argv[2:]:
#     plt.scatter(marks[arg], exp, alpha=0.5)
# plt.yscale("log")
# plt.scatter(marks[sys.argv[3]], exp, alpha=0.2, c = 'green')
# plt.scatter(marks[sys.argv[2]], exp, alpha=0.2, c = 'orange')
plt.savefig("test.png")
plt.close()