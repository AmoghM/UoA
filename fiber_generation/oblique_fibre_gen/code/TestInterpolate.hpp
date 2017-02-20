 #include <cxxtest/TestSuite.h>
#include "TrianglesMeshReader.hpp"
#include "TetrahedralMesh.hpp"
#include <iostream>
#include <fstream>
#include <vector>
#include "PetscSetupAndFinalize.hpp"
// #include <c_vector>
#include "VtkMeshWriter.hpp"
// #include "AbstractConductivityModifier.hpp"
 #include <AbstractTetrahedralMesh.hpp>
// #include <MeshReader.hpp>
#include <AbstractMeshReader.hpp>
#include "TrianglesMeshReader.hpp"
#include <math.h>
//#include "cvector.h"
// #include <boost/numeric/ublas/vector.hpp>
// #include <boost/numeric/ublas/vector_expression.hpp>
// #include <boost/numeric/ublas/traits/c_array.hpp>
#include <string>
using namespace std;
#define PI 3.14159265
class TestCuboid : public CxxTest::TestSuite
{

// public:
//   void TestRotate();

std::vector<c_vector<double,3u> > sheet_directions;
std::vector<c_vector<double,3u> > cross_directions;
std::vector<c_vector<double,3u> > fibre_directions;

public:
    void TestRotate(std::vector<double> data)
    {
       c_vector<double, 3u> sheet_direction;
       c_vector<double, 3u> cross_direction;
       c_vector<double, 3u> fibre_direction;

  

      double angle=data[0];
      double centroid_x=data[1];
      double centroid_y=data[2];
      double centroid_z=data[3];

      sheet_direction(0)=1;
      sheet_direction(1)=0;
      sheet_direction(2)=0;

      cross_direction(0)=0;
      cross_direction(1)=1;
      cross_direction(2)=0;

      fibre_direction(0)=0;
      fibre_direction(1)=0;
      fibre_direction(2)=1;

      if (centroid_z< 0.5/3)
      {
        sheet_directions.push_back(sheet_direction);
        cross_directions.push_back(cross_direction);
        fibre_directions.push_back(fibre_direction);
              // cout<<"1st: " << centroid_z<<endl;
      }
          
      else if (centroid_z>=(0.5/3) && centroid_z<=(1.0/3)) 
      {
        double res_cos=cos ( angle * M_PI / 180.0 );
        double res_sin=sin( angle * M_PI / 180.0 );
      
        double x=sheet_direction(0);
        double y=sheet_direction(1);
        double z=sheet_direction(2);
        
        sheet_direction(0)= x*res_cos-y*res_sin;
        sheet_direction(1)= x*res_sin+y*res_cos;
        sheet_direction(2)= z;

        x=cross_direction(0);
        y=cross_direction(1);
        z=cross_direction(2);

        cross_direction(0)=x*res_cos-y*res_sin;
        cross_direction(1)=x*res_sin+y*res_cos;
        cross_direction(2)=z;

        x=fibre_direction(0);
        y=fibre_direction(1);
        z=fibre_direction(2);

        fibre_direction(0)=x*res_cos-y*res_sin;
        fibre_direction(1)=x*res_sin+y*res_cos;
        fibre_direction(2)=z;



        sheet_directions.push_back(sheet_direction);
        cross_directions.push_back(cross_direction);
        fibre_directions.push_back(fibre_direction);

        // cout<<"2nd"<<endl;
      }

         else if (centroid_z>(1.0/3))
        {
            sheet_directions.push_back(sheet_direction);
            cross_directions.push_back(fibre_direction);
            fibre_directions.push_back(cross_direction);
          // cout<<"3rd: " <<centroid_z <<endl;
       }

}


public:
    void TestRead() throw(Exception)
    {  
     
      // std::vector<c_vector<double,3u> > fibre_directions;
      // std::vector<c_vector<double,3u> > sheet_directions;
      // std::vector<c_vector<double,3u> > cross_directions;

      TrianglesMeshReader<3,3> mesh_reader("/people/amis080/Desktop/fibre/tran/cuboid_mesh2.2");
      TetrahedralMesh<3,3> mesh; 
      mesh.ConstructFromMeshReader(mesh_reader);
      
      string line;
      ifstream myfile("/people/amis080/Desktop/interpolated_data22");
      
      if(myfile.is_open())
      {
         while(getline(myfile, line))
         {
          vector<double> numbers;
          istringstream ss(line);
          string token;
          while(std::getline(ss, token, ' '))
          {
            // cout << line<<"\n"<<endl;
            // std::cout << token << endl;
            // numbers.push_back(stod(token));
          numbers.push_back(atof(token.c_str()));
          }
          
          TestRotate(numbers);
          // cout << numbers[0]<<endl;
        }
         myfile.close();
      }
      TestVisualise();
}

  public:
    void TestVisualise()
    {
      TrianglesMeshReader<3,3> mesh_reader("/people/amis080/Desktop/fibre/tran/cuboid_mesh2.2");
      TetrahedralMesh<3,3> mesh; 
      mesh.ConstructFromMeshReader(mesh_reader);

      VtkMeshWriter<3u, 3u> mesh_writer("mesh_output", "mesh_oblique", false);
      mesh_writer.AddCellData("Fibre Direction", fibre_directions);
      mesh_writer.AddCellData("Sheet Direction", sheet_directions);
      mesh_writer.AddCellData("Cross Direction", cross_directions);
      mesh_writer.WriteFilesUsingMesh(mesh);
    }

};







































