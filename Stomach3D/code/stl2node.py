import os
def generation():
	#stl_files=os.listdir("./hsb016_cmgui_mesh_together/hsb016_cmgui_mesh_stl")
	path="/people/amis080/Desktop/stomach3D/hsb016_cmgui_mesh_together"
	stl_files=os.listdir(path+"/hsb016_cmgui_mesh_stl")
	

	for i in range(0,len(stl_files)):
		file=path+"/hsb016_cmgui_mesh_stl/"+stl_files[i]
		search="vertex"
		with open(path+"/nodes/"+stl_files[i][:-4]+".node", "w") as wtr:	
			wtr.write("Every 3 lines form a triangle with themselves. Every line represents x,y,z coordinate\n")
			with open(file,"r") as f:
				for itr in f:
					if (itr.find(search) is not -1):
						new_arr=' '.join(itr.split())
						wtr.write(new_arr[7:]+"\n")	 
			f.close()
		wtr.close()

if __name__ == '__main__':
	generation()

