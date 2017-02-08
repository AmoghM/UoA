import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("surface1")
ax= fig.add_subplot(111, projection='3d')


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
with open("output_surface1.1") as f:
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
with open("output_surface2.1") as f:
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
with open("output_surface3.1") as f:
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
with open("output_surface4.1") as f:
	f.readline()
	for i in f:
		i=' '.join(i.split(","))
		i=i.split(" ")
		print i
		x4.append(float(i[0]))
		y4.append(float(i[1]))
		z4.append(float(i[2]))



# # m2=[-30.541,162.887,-248.553]
# m2=[-27.764745693679806,172.78633734565946,-259.54639878477093]

# missed=[-24.649387067,177.989161055,-240.308007464]
missed=[-24.3822881665,177.902715325,-239.712083678]

ax1.scatter(x1, y1, z1, c="yellow")
ax2.scatter(x2, y2, z2, c="yellow")
ax3.scatter(x3, y3, z3, c="yellow")
ax4.scatter(x4, y4, z4, c="yellow")

ax1.scatter(missed[0],missed[1],missed[2], c="red",marker='^')

ax2.scatter(missed[0],missed[1],missed[2], c="red",marker='^')

ax3.scatter(missed[0],missed[1],missed[2], c="red",marker='^')

ax4.scatter(missed[0],missed[1],missed[2], c="red",marker='^')




# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

plt.show()
