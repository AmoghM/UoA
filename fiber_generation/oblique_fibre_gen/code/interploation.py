import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate


fig = plt.figure("cuboid")
ax= fig.add_subplot(111, projection='3d')




x=[0,3]
y=[0,2]
z=[[45,30],[60,45]]

x1=[]
y1=[]
z1=[]
function=interpolate.interp2d(x,y,z)
interpolated=[]
with open("interpolated_data22","w") as itr:
	with open("output2") as f:
		for i in f:
			i=' '.join(i.split(","))
			i=i.split(" ")
			
			x_val=float(i[0])
			y_val=float(i[1])
			z_val=float(i[2])

			val=function(x_val,y_val)
			# print val[0]
			interpolated.append(val[0])
			
			x1.append(x_val)
			y1.append(y_val)
			z1.append(z_val)

			data= str(val[0])+" " +i[0]+" "+i[1]+" "+i[2]
			print data
			itr.write(data)
			
			
	f.close()
itr.close()

ax.scatter(x1, y1, z1, c="yellow")
# ax.scatter(x1,y1,interpolated, c='red')
plt.show()
