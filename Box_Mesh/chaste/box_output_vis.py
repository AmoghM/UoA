from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

n_angles = 36
n_radii = 8
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
x=[]
y=[]
z=[]
with open("/tmp/amis080/testoutput/BoxOutput/linear_solution-1.txt") as f:
	for i in f:
		i=i.split(" ")
		x.append(float(i[0]))
		y.append(float(i[1]))
		z.append(float(i[2]))
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)

plt.show()
