import numpy as np
import matplotlib.pyplot as plt


x = []
y = []
N=50
with open("./data/box") as f:
	for i in f:
		i=' '.join(i.split())
		i=i.split(" ")
		print i
		x.append(float(i[1]))
		y.append(float(i[2]))

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
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))
plt.scatter(x, y, s=area, alpha=0.5)
plt.show()