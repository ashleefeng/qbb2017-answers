#!/usr/bin/env python

"""
./scatter.py <x.ctab> <y.ctab> <output>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

epsilon = 1e-3

x_ctab_fn = sys.argv[1]
y_ctab_fn = sys.argv[2]
output_fn = sys.argv[3]

xdf = pd.read_csv(x_ctab_fn, sep='\t')
ydf = pd.read_csv(y_ctab_fn, sep='\t')

fig = plt.figure()
ax = fig.gca()
# plt.scatter(np.log(xdf["FPKM"]), np.log(ydf["FPKM"]))
# print xdf["FPKM"].head()
plt.yscale("log")
plt.xscale("log")
plt.title("FPKM scatter plot")
plt.xlabel(x_ctab_fn)
plt.ylabel(y_ctab_fn)


fit = np.polyfit(xdf["FPKM"], ydf["FPKM"],1)
p = np.poly1d(fit)
xp = np.logspace(-3, 4, 100)

plt.scatter(xdf["FPKM"], ydf["FPKM"], alpha=0.1)
plt.plot(xp, p(xp), '--', color='r')

plt.savefig(output_fn + '.png')
plt.close()

xy = np.ndarray(shape=(2, len(xdf["FPKM"])))
xy[0] = xdf["FPKM"]
xy[1] = ydf["FPKM"]
xy = np.log(xy + epsilon)
madf = pd.DataFrame(xy)
plt.figure()

plt.scatter(madf.mean(axis=0), xy[1] - xy[0])
plt.title("MA plot")
plt.xlabel("A")
plt.ylabel("M")
plt.savefig(output_fn + '_MA.png')
plt.close