import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from surface_normal import face_reader
fr=face_reader()
x = []
y = []
z=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in fr:
	x.append(float(i[0]))
	y.append(float(i[1]))
	z.append(float(i[2]))

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
#colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))
ax.scatter(x, y, z, c="yellow")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()