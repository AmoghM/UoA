import os
def generation():
	#stl_files=os.listdir("./hsb016_cmgui_mesh_together/hsb016_cmgui_mesh_stl")
	path="/people/amis080/Desktop/stomach3D/hsb016_cmgui_mesh_together"
	stl_files=os.listdir(path+"/hsb016_cmgui_mesh_stl")
	

	for i in range(0,len(stl_files)):
		file=path+"/hsb016_cmgui_mesh_stl/"+stl_files[i]
		search="facet normal"
		with open(path+"/normal/"+stl_files[i][:-4]+".normal", "w") as wtr:	
			with open(file,"r") as f:
				for itr in f:
					if (itr.find(search) is not -1):
						new_arr=' '.join(itr.split())
						print new_arr
						wtr.write(new_arr[12:]+"\n")	 
			f.close()
		wtr.close()

if __name__ == '__main__':
	generation()

