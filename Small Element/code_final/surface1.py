# from barycentre_triangle import barycentre as bc
# from bary import bary
# from projection import DoesLies as dl
from exist import exist
from face2node import getcoord
def extract():
	with open('small_element_sur_1.node') as f:
		f.readline()
		node=[]
		triangle=[]
		count=0
		for i in f:
			if count<3:
				node.append(i)
				count+=1
			else:
				triangle.append(node)
				node=[]
				node.append(i)
				count=1
				#break
	f.close()
	return triangle

def create(): #creates the 3 layer nested list of list.
	dat=extract()
	dataset=[]
	for i in dat:
		node=[]
		for j in i:
			tmp=map(float, j.split())
			node.append(tmp)
		dataset.append(node)
	# print dataset
	return dataset

# def read():
	# points=[]
	# with open("small_element_full.1.node") as f:
	# 	line=f.readlines()[1:-1]
	# 	for i in line:
	# 		tmp=map(float, i.split())
	# 		points.append(tmp[1:])
	
	# f.close()
	# points=[-21.1996,181.935,-248.351]
	# points=[-30.541,162.887,-248.553]
	
	# points=[-20.578975,180.25125,-255.352]
	

def isPresent():
	# pts=read()
	# btm=create()
	# dist_list=[]
	# for itr in pts:
	# 	for bt in btm: 
	# 		ar=dl(bt,itr)
	# 		dist_list.append(ar)
	# 		if dl(bt,itr) is True:
	# 			print "ahem"
	# print "MINIMUM DISTANCE", min(dist_list)		
			# if bc(bt,itr) is True:
			# 	print "Found it"
			# 	exit()
			# else:
			# 	print "Searching"
	# for itr in pts:
	# for bt in btm:
	# 	exist(bt[0],bt[1],bt[2],pts)
	cc=getcoord()
	#cc=[[-27.764745693679806,172.78633734565946,-259.54639878477093]]
	btm=create()
	with open("output_surface1.2","w") as wt:	
		with open("missed_surface1.2","w") as wt2:	
			for i in cc:
				dist_list=[]
				dist_list2=[]
				for bt in btm:
					distance=exist(bt[0],bt[1],bt[2],i)
					# res=bary(bt[0],bt[1],bt[2],i)
					if distance < 0.1:
						dist_list.append(distance)
					
					elif distance!=1000 and distance>=0.1:
						dist_list2.append(distance)

				if len(dist_list)>0:
					for item in i:
						wt.write("%s,"%item)
					wt.write(str(min(dist_list)))
					wt.write("\n")

				if len(dist_list2)>0:
					for item in i:
						wt2.write("%s,"%item)
					# wt2.write(str(min(dist_list2)))
					wt2.write("\n")
		wt2.close()
	wt.close()
			



if __name__ == '__main__':
	isPresent()

