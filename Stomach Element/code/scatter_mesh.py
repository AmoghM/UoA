import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = []
y = []
z=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

with open("./data/stomach_element") as f:
	for i in f:
		i=' '.join(i.split())
		i=i.split(" ")
		print i
		x.append(float(i[1]))
		y.append(float(i[2]))
		z.append(float(i[3]))

print "the coordinate of x are:"
print x
print "************************"

print "the coordinate of y are:"
print y
print "************************"

print "Minimum X is: ", min(x)
print "Minimum Y is:", min(y)
print "Maximum X is:", max(x)
print "Minimum Y is:", max(y)

ax.scatter(x, y, z, c="yellow")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
