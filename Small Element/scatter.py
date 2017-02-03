import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



fig1 = plt.figure("surface1")
ax1 = fig1.add_subplot(111, projection='3d')

fig2=plt.figure("surface2")
ax2 = fig2.add_subplot(111, projection='3d')

fig3=plt.figure("surfac3")
ax3 = fig3.add_subplot(111, projection='3d')

fig4=plt.figure("surface4")
ax4 = fig4.add_subplot(111, projection='3d')



x1 = []
y1 = []
z1=[]
with open("SURFACE1") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(","))
		i=i.split(" ")
		print i
		x1.append(float(i[0]))
		y1.append(float(i[1]))
		z1.append(float(i[2]))


x2 = []
y2 = []
z2=[]
with open("SURFACE2") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(","))
		i=i.split(" ")
		print i
		x2.append(float(i[0]))
		y2.append(float(i[1]))
		z2.append(float(i[2]))


x3 = []
y3 = []
z3=[]
with open("SURFACE3") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(","))
		i=i.split(" ")
		print i
		x3.append(float(i[0]))
		y3.append(float(i[1]))
		z3.append(float(i[2]))


x4 = []
y4 = []
z4=[]
with open("SURFACE4") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(","))
		i=i.split(" ")
		print i
		x4.append(float(i[0]))
		y4.append(float(i[1]))
		z4.append(float(i[2]))

ax1.scatter(x1, y1, z1, c="yellow")

ax2.scatter(x2, y2, z2, c="yellow")
ax3.scatter(x3, y3, z3, c="yellow")
ax4.scatter(x4, y4, z4, c="yellow")
plt.show()
