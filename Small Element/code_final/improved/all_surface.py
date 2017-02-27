from exist import exist
from face2node import getcoord
import os

def extract(path):
	data_list=[]
	with open(path) as f:
		f.readline()
		count=0;
		l=f.readlines()
		ll=[]
		for x in range(0,256):
			node=[]
			node.append(l[(3*x)+0])
			node.append(l[(3*x)+1])
			node.append(l[(3*x)+2])

			ll.append(node)
	f.close()
	return ll

def create(path):
	dataset=extract(path)
	preprocess=[]
	for i in dataset:
		temp=[]
		for j in range(0,3):
			node=map(float, i[j].split())
			temp.append(node)
		preprocess.append(temp)

	#preprocess contains 256 triangle nodes. each index points towards a set of 3 triangle nodes of the form (x,y,z)
	return preprocess

def isPresent():

	path="/people/amis080/Desktop/smaller/code_final/data_surface"
	direct=['small_element_sur_1.node', 'small_element_sur_2.node', 'small_element_sur_3.node', 'small_element_sur_4.node']
	cc=getcoord()
	with open("all_surface_classified2","w") as wt, open("all_surface_missed2","w") as wt2:
		for i in cc:
			dist_min=[100.0]*4
			ex=False
			for file in range(0,len(direct)):
				file_path=path+"/"+direct[file]
				btm=create(file_path)
				flag=0
				dist_found=[]
				for bt in btm:
					distance=exist(bt[0],bt[1],bt[2],i)
					if distance <= 0.8:
						dist_found.append(distance)
						flag+=1;

				if flag>0:
					dist_min[file]=min(dist_found)
					ex=True

			if ex is True:
				for j in i:
					wt.write("%s,"%j)
				minimum=min(dist_min)
				wt.write(str(minimum)+",")
				wt.write(str(dist_min.index(minimum)+1))
				wt.write("\n")
			
			else:
				st=""
				for j in i:
					st=st+str(j)+","
				wt2.write(st[:-2])
				wt2.write("\n")

	wt.close()
	wt2.close()
			



if __name__ == '__main__':
	isPresent()