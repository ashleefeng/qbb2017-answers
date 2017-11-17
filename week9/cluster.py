#! /usr/bin/env python

import numpy as np
import scipy.cluster as sc
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq

df = pd.read_csv('hema_data.txt', delimiter='\t')

data = df.as_matrix()[:, 1:].astype(float)

linkage_matrix = sc.hierarchy.linkage(data, method='average')

heatmap_order = sc.hierarchy.leaves_list(linkage_matrix)

ordered_data = data[heatmap_order, :]

plt.figure()

plt.pcolor(ordered_data)

# plt.savefig('heatmap.png')

plt.close()

linkage_matrixT = sc.hierarchy.linkage(data.T, method='average')
heatmap_orderT = sc.hierarchy.leaves_list(linkage_matrixT)
col = list(df.columns.values)[1:]
ordered_col = [col[i] for i in heatmap_orderT]

plt.figure()

den = sc.hierarchy.dendrogram(linkage_matrixT,labels=col)

plt.title('Dendrogram')

# plt.savefig('dendrogram.png')

plt.close()

centroids,_ = kmeans(data, 6, iter=100)
idx,_ = vq(data, centroids)

plt.plot(data[idx==0, 0], data[idx==0,1],'ob', data[idx==1,0],data[idx==1,1], 'or', data[idx==2, 0], data[idx==2,1],'og', data[idx==3, 0], data[idx==3,1],'oy', data[idx==4, 0], data[idx==4,1],'oc', data[idx==5, 0], data[idx==5,1], 'om')

plt.xlabel('CFU')
plt.ylabel('poly')

plt.title('k-means clustering')

plt.plot(centroids[:,0], centroids[:, 1], 'sk', markersize=8)
plt.savefig('k-means.png')


