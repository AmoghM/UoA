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
	print coord
	return coord


 
if __name__ == '__main__':
	nodes=getnodes()
	coordinates=getcoord()
