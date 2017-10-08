#! /usr/bin/python

import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt

val_filename = sys.argv[1]
vec_filename = sys.argv[2]
out_filename = sys.argv[3]

vals = np.loadtxt(val_filename)
vecs = np.loadtxt(vec_filename, usecols = [2, 3])

pca = vals * vecs

plt.figure()

plt.scatter(pca[:, 0], pca[:, 1])
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('Principle component analysis')

plt.savefig(out_filename + '.png')
plt.close()

