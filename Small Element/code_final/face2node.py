import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def getnodes():
	set_nodes=set()
	with open("small_element_full.1.face") as face:
			ff=face.readlines()[1:-1]
			for arr in ff:
				itr=arr.split()
				for i in range(1,4):
					set_nodes.add(int(itr[i]))
	face.close()
	# print len(set_nodes) 18332 points only found.
	
	return set_nodes

def getcoord():
	nodes=getnodes()
	coord=[]
	with open("small_element_full.1.node") as n:
		nn=n.readlines()[1:-1]
	n.close()
	

	for i in nodes:
		coord.append(map(float,nn[int(i-1)].split()[1:]))
	
	# print coord
	# x=[]
	# y=[]
	# z=[]	
	# for i in coord:
	# 	x.append(i[0])
	# 	y.append(i[1])
	# 	z.append(i[2])
	# fig1 = plt.figure("surface1")
	# ax1 = fig1.add_subplot(111, projection='3d')

	# x.append(float(i[0]))
	# y.append(float(i[1]))
	# z.append(float(i[2]))

	# ax1.scatter(x, y, z, c="yellow")
	# plt.show()
	return coord

# # m2=[-30.541,162.887,-248.553]
# m2=[-27.764745693679806,172.78633734565946,-259.54639878477093]




 
if __name__ == '__main__':
	nodes=getnodes()
	coordinates=getcoord()
