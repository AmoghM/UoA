import numpy as np
def exist(p1,p2,p3,p):
	u=np.subtract(p2,p1)
	v=np.subtract(p3,p1)
	w=np.subtract(p,p1)

	n=np.cross(u,v)
	mag=sum(map(lambda x:x*x,n))

	g_cross=np.cross(u,w)
	b_cross=np.cross(w,v)

	gamma=float(np.dot(g_cross,n))/mag
	beta=float(np.dot(b_cross,n))/mag
	alpha=1-gamma-beta

	x=np.multiply(p1,alpha)
	y=np.multiply(p2,beta)
	z=np.multiply(p3,gamma)

	foot=map(sum, zip(x,y,z))

	p=np.array(p)
	if gamma >=0 and gamma <=1 and beta >=0 and beta <=1 and alpha >=0 and alpha <=1:
		dist= np.linalg.norm(foot-p)
# if __name__ == '__main__':
# 	p1=[-20.504449999999999,180.6155,-255.13049999999998]
# 	p2=[ -20.704474999999999,180.77525,-255.61574999999999]
# 	p3=[-20.578975,180.25125,-255.352]
# 	p=[-20.578975,180.25125,-255.352]
# 	print exist(p1,p2,p3,p)
