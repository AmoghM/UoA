#http://math.stackexchange.com/questions/544946/determine-if-projection-of-3d-point-onto-plane-is-within-a-triangle
import numpy as np

def DoesLies(m1,m2):
	u=np.subtract(m1[1],m1[0])
	v=np.subtract(m1[2],m1[0])
	w=np.subtract(m2,m1[0])

	n=np.cross(u,v)

	gamma= np.dot((np.cross(u,w)),n)/(np.linalg.norm(n)**2)
	beta=np.dot((np.cross(w,v)),n)/(np.linalg.norm(n)**2)
	alpha = 1-gamma-beta
	
    #P=alpha P1+ beta P2+ gamma P3
	x=np.multiply(m1[0],alpha)
	y=np.multiply(m1[1],beta)
	z=np.multiply(m1[2],gamma)

	foot=map(sum, zip(x,y,z))
	
    #distance of the foot of the perpendicular with the point P
	foot=np.array(foot)
	print "Foot is:", foot
	dist= np.linalg.norm(foot-m2)
	if gamma >=0 and gamma <=1 and beta >=0 and beta <=1 and alpha >=0 and alpha <=1:
		print "exist"
	else:
		print "doesn't exist"

	return dist

# if __name__ == '__main__':
	# m1=[[0,0,0],[0,2,0],[2,0,0]]
	# m2=[-10,1,0]
	
	# DoesLies(m1,m2)
