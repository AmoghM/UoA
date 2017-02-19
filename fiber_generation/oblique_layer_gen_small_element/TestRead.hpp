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
class TestCube : public CxxTest::TestSuite
{

public:
    void Testvisualise() throw(Exception)
    {  
     

      std::vector<c_vector<double,3u> > sheet_directions;
      std::vector<c_vector<double,3u> > cross_directions;
      std::vector<c_vector<double,3u> > fibre_directions;

       c_vector<double, 3u> sheet_direction;
       c_vector<double, 3u> cross_direction;
       c_vector<double, 3u> fibre_direction;
      
        TrianglesMeshReader<3,3> mesh_reader("/people/amis080/Desktop/fibre/tran/cuboid_mesh2.2");
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

          ofstream outputFile;
          outputFile.open("/people/amis080/Desktop/output",ios_base::app);

          outputFile << xx << "," << yy << "," << zz<<endl;

          }
      }
};



