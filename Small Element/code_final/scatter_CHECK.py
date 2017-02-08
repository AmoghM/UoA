import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = []
y = []
z=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


fig2=plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
# with open("small_element_sur_2.node") as f:
with open("OUTPUT.merge") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(','))
		i=i.split(" ")
		print i
		x.append(float(i[0]))
		y.append(float(i[1]))
		z.append(float(i[2]))

# m2=[-30.541,162.887,-248.553]
# m2=[-27.764745693679806,172.78633734565946,-259.54639878477093]
# missed=[-24.649387067,177.989161055,-240.308007464]
missed=[-24.3822881665,177.902715325,-239.712083678]
ax.scatter(x, y, z, c="yellow")
# ax.scatter(m2[0],m2[1],m2[2], c="red",marker='^')
ax.scatter(missed[0],missed[1],missed[2], c="red",marker='^')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
