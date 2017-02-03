import numpy as np
def bary(p1,p2,p3,p):
	AB=np.subtract(p2,p1)
	BC=np.subtract(p3,p2)
	AC=np.subtract(p3,p1)

	PB=np.subtract(p2,p)
	PC=np.subtract(p3,p)
	PA=np.subtract(p1,p)

	area=float(np.linalg.norm(np.cross(AB,AC)))/2

	alpha=float(np.linalg.norm(np.cross(PB,PC)))/2
	beta=float(np.linalg.norm(np.cross(PC,PA)))/2
	gamma=1-alpha-beta

	if alpha>=0 and alpha<=1 and beta>=0 and beta<=1 and gamma>=0 and gamma<=1:
		return True
	else:
		return False

# if __name__ == '__main__':
# 	p1=[-20.504449999999999,180.6155,-255.13049999999998]
# 	p2=[ -20.704474999999999,180.77525,-255.61574999999999]
# 	p3=[-20.578975,180.25125,-255.352]
# 	p=[-20.578975,180.25125,-255.352]
# 	bary(p1,p2,p3,p)