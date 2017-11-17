#! /usr/bin/env python

import numpy as np
import scipy.cluster as sc
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq
from scipy import stats

df = pd.read_csv('hema_data.txt', delimiter='\t')

data = df.as_matrix()[:, 1:].astype(float)

linkage_matrix = sc.hierarchy.linkage(data, method='average')

heatmap_order = sc.hierarchy.leaves_list(linkage_matrix)

ordered_data = data[heatmap_order, :]

plt.figure()

plt.pcolor(ordered_data)

# plt.savefig('heatmap.png')

plt.close()

# dendrogram

linkage_matrixT = sc.hierarchy.linkage(data.T, method='complete')
heatmap_orderT = sc.hierarchy.leaves_list(linkage_matrixT)
col = list(df.columns.values)[1:]
ordered_col = [col[i] for i in heatmap_orderT]

plt.figure()

den = sc.hierarchy.dendrogram(linkage_matrixT,labels=col)

plt.title('Dendrogram')

# plt.savefig('dendrogram_complete.png')

plt.close()
 
# k-means clustering

centroids,_ = kmeans(data, 6, iter=100)
idx,_ = vq(data, centroids)

plt.plot(data[idx==0, 0], data[idx==0,1],'ob', data[idx==1,0],data[idx==1,1], 'or', data[idx==2, 0], data[idx==2,1],'og', data[idx==3, 0], data[idx==3,1],'oy', data[idx==4, 0], data[idx==4,1],'oc', data[idx==5, 0], data[idx==5,1], 'om')

plt.xlabel('CFU')
plt.ylabel('poly')

plt.title('k-means clustering')

plt.plot(centroids[:,0], centroids[:, 1], 'sk', markersize=8)
# plt.savefig('k-means.png')

# differential expression

cfu = data[:, 0]
mys = data[:, 4]

poly = data[:, 1]
unk = data[:, 2]

early = np.ndarray(shape=(len(data), 2))
early[:, 0] = cfu
early[:, 1] = mys

late = np.ndarray(shape=(len(data), 2))
late[:, 0] = poly
late[:, 1] = unk

# for i in range(len(data)):
#     tstats, p = stats.ttest_rel(early[i, :], late[i, :])
#     if p <= 0.05:
#        print str(df['gene'][i]) + '\t' +  str(p)

temp_max = 0
temp_gene = ''
temp_idx = 0

for i in range(len(data)):
    tstats, p = stats.ttest_rel(early[i, :], late[i, :])
    early_avg = np.mean(early[i, :])
    late_avg = np.mean(late[i, :])
    if (p <= 0.05) and (early_avg < late_avg):
        curr = late_avg/early_avg
        if curr > temp_max:
            temp_idx = i
            temp_max = curr
            temp_gene = df['gene'][i]

genes = df['gene'][idx==idx[i]].as_matrix()

for j in genes:
    print j + ',',
