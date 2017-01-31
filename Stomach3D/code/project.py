from barycentre_triangle import barycentre as bc
from projection import DoesLies as dl
def extract():
	with open('curve_top.node') as f:
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

def read():
	points=[]
	with open("hsb16_tesel_4.1.node") as f:
		line=f.readlines()[1:-1]
		for i in line:
			tmp=map(float, i.split())
			points.append(tmp[1:])
	
	f.close()
	return points

def isPresent():
	pts=read()
	btm=create()
	for itr in pts:
		for bt in btm: 
			if dl(bt,itr) is True:
				print "ahem"
				exit()

if __name__ == '__main__':
 	isPresent()

