'''
This code uses the barycentric technique of evaluating whether a point lies inside the triangle of not.
To compute: P= A+ u*(C-A)+ v*(B-A) where A,B,C are vertices of the traingle and P is the point to be checked to lie in the triangle.
Condition to check: if u,v <0 or u,v>0 or u+v>1: point P doesn't lie inside the triangle
Whereas, if u>=0 and v>=0 and u+v<1: Point P lies inside the traingle

Guide: http://blackpawn.com/texts/pointinpoly/
'''
import numpy as np

def bary_tra(m1,m2): #m1 matrix dimensions should be 3*3 and m2 should be 1*3
	vec_v2=np.subtract(m2,m1[0])
	vec_v0=np.subtract(m1[2],m1[0])
	vec_v1=np.subtract(m1[1]-m1[0])

	#Computing the dot products
	dot00=np.dot(vec_v0,vec_v0)
	dot01=np.dot(vec_v0,vec_v1)
	dot02=np.dot(vec_v0,vec_v2)
	dot11=np.dot(vec_v1,vec_v1)
	dot12=np.dot(vec_v1,vec_v2)

	#Computing the Barycentric coordinate
	invDenom=1/((dot00*dot11)-(dot01*dot11))

	#Computing the coefficient
	u=((dot11*dot02) - (dot01*dot12))*invDenom
	v=((dot00*dot12) - (dot01*dot02))*invDenom

	#Check if the point lies

	return ((u>=0) && (v>=0) && (u+v<1))
