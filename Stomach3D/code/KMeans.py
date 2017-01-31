import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
style.use("ggplot")

from sklearn.cluster import KMeans
from surface_normal import face_reader

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X=face_reader()
kmeans=KMeans(n_clusters=1, max_iter=300)
kmeans.fit(X)

centroids=kmeans.cluster_centers_  #returns the 6 points representing the indivual clusters
labels =kmeans.labels_ #tells which instance belongs to which cluster #

print centroids
print labels
print len(labels)
colors = ["g"]

for i in range(0,len(centroids)):
  	ax.scatter(centroids[i][0], c='r', marker = "x", linewidths = 5, zorder = 10)

for i in range(0,len(X)):
	ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()