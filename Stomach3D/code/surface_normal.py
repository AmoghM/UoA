import numpy as np
def normal(p1,p2,p3):
	v=np.subtract(p2,p1)
	w=np.subtract(p3,p1)

	#nx=(vy*wz)-(vz*wy)
	nx=(v[1]*w[2])-(v[2]*w[1])
	#ny=(vz*wx)-(vx*wz)
	ny=(v[2]*w[0])-(v[0]*w[2])
	#nz=(vx*wy)-(vy*wx)
	nz=(v[0]*w[1])-(v[1]*w[0])

	mag=np.sqrt((nx**2)+(ny**2)+(nz**2))
	vec_norm[0]=float(nx/mag)
	vec_norm[1]=float(ny/mag)
	vec_norm[2]=float(nz/mag)
	#print vec_norm
	return vec_norm

def node_reader():
	node_arr=[]
	with open("bottom.node") as node:
		node.readline()
		for line in node:
			line=' '.join(line.split( ))
			line=line.split(" ")
			tup=[float(line[0]),float(line[1]),float(line[2])]
			node_arr.append(tup)
	return node_arr


def face_reader():
	
	surface_normal=[]
	nodes=node_reader()
	for line in range(0,len(nodes)-2):
		surface_normal.append(normal(nodes[line],nodes[line+1],nodes[line+2]))
	return surface_normal

if __name__ == '__main__':
	face_reader()