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
df_exp['sort'] = df_exp['t_name'].str.extract('(\d+)', expand=False).astype(int)
# print df_exp['t_name'].str.extract('(\d+)', expand=False)[2]
df_exp = df_exp.sort_values("sort")
df_exp = df_exp.reset_index(drop=True)
# print df_exp.head()
marks = []

for arg in sys.argv[2:]:

    df_mark = pd.read_csv(arg, sep='\t', header=None, names = ["name", "size", "covered", "sum", "mean0", "mean"])
    df_mark['sort'] = df_mark['name'].str.extract('(\d+)', expand=False).astype(int)
    df_mark = df_mark.sort_values("sort")
    # print df_mark.head()
    df_mark = df_mark.reset_index(drop=True)
    marks.append(df_mark["mean"])

marks = pd.DataFrame(marks, index = sys.argv[2:])
marks = marks.T

# exp = np.log1p(df_exp["FPKM"])
exp = df_exp["FPKM"]
exp = exp.T
roi = exp > 0.0

# print marks[roi]
# print exp[roi]

# mod = sm.OLS(exp[roi], marks[roi])

# print exp.head()
# print marks.head()
mod = sm.OLS(exp, marks)
# print marks
# marks = sm.add_constant(marks) # not sure why
res = mod.fit()
print "p values:"
print res.pvalues
print "mean of residual squares"
print res.mse_total
print res.summary()

plt.figure()

# plt.scatter(exp[roi], res.predict().T, alpha = 0.1)
plt.scatter(exp, res.predict().T, alpha = 0.1)

# plt.plot(marks, exp, '.')
# for arg in sys.argv[2:]:
#     plt.scatter(marks[arg], exp, alpha=0.5)
# plt.yscale("log")
# plt.scatter(marks[sys.argv[3]], exp, alpha=0.2, c = 'green')
# plt.scatter(marks[sys.argv[2]], exp, alpha=0.2, c = 'orange')
plt.savefig("test.png")
plt.close()