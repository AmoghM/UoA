#include <cxxtest/TestSuite.h>
#include "TrianglesMeshReader.hpp"
#include "TetrahedralMesh.hpp"
#include <iostream>
#include <fstream>
#include <vector>
class TestCube : public CxxTest::TestSuite
{
public:
    void visualise() throw(Exception)
    {  
       string line;
       c_vector<double, 3u> sheet_direction;
       c_vector<double, 3u> cross_direction;
       c_vector<double, 3u> fibre_direction;

       for (int i=1;i<=195;i++)
       {
            sheet_direction.push_back(1);
            sheet_direction.push_back(0);
            sheet_direction.push_back(0);
            
            cross_direction.push_back(0);
            cross_direction.push_back(1);
            cross_direction.push_back(0);

            fibre_direction.push_back(0);
            fibre_direction.push_back(0);
            fibre_direction.push_back(1);
       }
        TrianglesMeshReader<2,2> mesh_reader("cube_mesh2.1");
        TetrahedralMesh<2,2> mesh; 
        mesh.ConstructFromMeshReader(mesh_reader);

        VtkMeshWriter<3u, 3u> mesh_writer("cube_mesh2.1", "mesh", false);
        mesh_writer.AddCellData("Fibre Direction", fibre_directions);
        mesh_writer.AddCellData("Sheet Direction", sheet_directions);
        mesh_writer.AddCellData("Cross Direction", cross_directions);
        mesh_writer.WriteFilesUsingMesh(mesh);
   
        return 0;
    }
};
