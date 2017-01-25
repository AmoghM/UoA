import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
style.use("ggplot")

from sklearn.cluster import AgglomerativeClustering
from surface_normal import face_reader

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X=face_reader()
agc=AgglomerativeClustering(n_clusters=6)
agc.fit(X)
labels=agc.labels_
colors = ["g", "r", "c" , "y", "b","k"]

for i in range(0,len(X)):
	ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()