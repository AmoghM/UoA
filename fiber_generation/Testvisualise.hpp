#include <cxxtest/TestSuite.h>
#include "TrianglesMeshReader.hpp"
#include "TetrahedralMesh.hpp"
#include <iostream>
#include <fstream>
#include <vector>
#include "PetscSetupAndFinalize.hpp"
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
class TestCube : public CxxTest::TestSuite
{

public:
    void Testvisualise() throw(Exception)
    {  
     

      std::vector<c_vector<double,3u> > sheet_directions;
      std::vector<c_vector<double,3u> > cross_directions;
      std::vector<c_vector<double,3u> > fibre_directions;

      // c_vector<double, 3u> sheet_direction = Create_c_vector(1,0,0);
      // c_vector<double, 3u> cross_direction = Create_c_vector(0,1,0);
      // c_vector<double, 3u> fibre_direction = Create_c_vector(0,0,1);

       c_vector<double, 3u> sheet_direction;
       c_vector<double, 3u> cross_direction;
       c_vector<double, 3u> fibre_direction;
   
        TrianglesMeshReader<3,3> mesh_reader("/people/amis080/Desktop/fibre/cube_mesh2.1");
        TetrahedralMesh<3,3> mesh; 
        mesh.ConstructFromMeshReader(mesh_reader);
        double angle=30;
        for(AbstractTetrahedralMesh<3,3>::ElementIterator elt_iter=mesh.GetElementIteratorBegin(); elt_iter!=mesh.GetElementIteratorEnd();++elt_iter)
        {
          sheet_direction(0)=1;
          sheet_direction(1)=0;
          sheet_direction(2)=0;

          cross_direction(0)=0;
          cross_direction(1)=1;
          cross_direction(2)=0;

          fibre_direction(0)=0;
          fibre_direction(1)=0;
          fibre_direction(2)=1;

          double xx=(elt_iter->CalculateCentroid())(0);
          double yy=(elt_iter->CalculateCentroid())(1);
          double zz=(elt_iter->CalculateCentroid())(2);

       

          if (zz< 0.5/3)
          {
              sheet_directions.push_back(sheet_direction);
              cross_directions.push_back(cross_direction);
              fibre_directions.push_back(fibre_direction);
              cout<<"1st: " << zz<<endl;
          }
          
         

          else if (zz>=(0.5/3) && zz<=(1.0/3)) 
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

            cout<<"2nd"<<endl;
          }

           else if (zz>(1.0/3))
          {
              sheet_directions.push_back(sheet_direction);
              cross_directions.push_back(fibre_direction);
              fibre_directions.push_back(cross_direction);
            cout<<"3rd: " <<zz <<endl;
         }
        }


        VtkMeshWriter<3u, 3u> mesh_writer("Desktop/fibre/ortho/omesh", "mesh9", false);
        mesh_writer.AddCellData("Fibre Direction", fibre_directions);
        mesh_writer.AddCellData("Sheet Direction", sheet_directions);
        mesh_writer.AddCellData("Cross Direction", cross_directions);
        mesh_writer.WriteFilesUsingMesh(mesh);
   
    }
};



