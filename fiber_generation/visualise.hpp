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
       
       // std::vector<c_vector<double,3u> > fibre_directions;
       // std::vector<c_vector<double,3u> > sheet_directions;
       // std::vector<c_vector<double,3u> > cross_directions;

       //  string line;
       //  ifstream myfile("cube_mesh2.1.ortho");
       //  if(myfile.is_open())
       //  {
       //      while(getline(myfile, line))
       //      {
             
       //          string disk=line;
       //          vector<string> cds;
       //          stringstream s (disk);
       //          while(s>>temp)
       //          {   cds.push_back(temp);}

       //          vector<string>::iterator v = cds.begin();
       //          int count=1;
       //          while( v != cds.end()) 
       //          {
                    
       //              if(count<=3)
       //              {
       //                  sheet_direction.push_back(*v)
       //              }

       //              else if(count<=6)
       //              {
       //                  cross_direction.push_back(*v);
       //              }

       //              else
       //                  fibre_direction.push_back(*v);
       //            count++;
       //            v++;
       //          }

       //          sheet_directions.push_back(sheet_direction);
       //          cross_directions.push_back(cross_direction);
       //          fibre_directions.push_back(fibre_direction);

       // }

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
