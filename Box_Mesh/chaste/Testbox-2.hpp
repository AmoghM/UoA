#include <cxxtest/TestSuite.h>
#include "UblasIncludes.hpp"
#include "SimpleLinearEllipticSolver.hpp"
#include "SimpleLinearParabolicSolver.hpp"
#include "SimplePoissonEquation.hpp"
#include "TrianglesMeshReader.hpp"
#include "TetrahedralMesh.hpp"
#include "BoundaryConditionsContainer.hpp"
#include "ConstBoundaryCondition.hpp"
#include "OutputFileHandler.hpp"
#include "PetscSetupAndFinalize.hpp"

class MyPde : public AbstractLinearEllipticPde<2,2>
{
private:
    c_matrix<double,2,2> mDiffusionTensor;

public:
    MyPde()
    {
        mDiffusionTensor(0,0) = 1.0;
        mDiffusionTensor(0,1) = 0.0;
        mDiffusionTensor(1,0) = 0.0;
        mDiffusionTensor(1,1) = 1.0;
    }

   double ComputeConstantInUSourceTerm(const ChastePoint<2>& rX, Element<2,2>* pElement)
    {
       return 0;
    }

    double ComputeLinearInUCoeffInSourceTerm(const ChastePoint<2>& rX, Element<2,2>* pElement)
    {
        return 0.0;
    }

    c_matrix<double,2,2> ComputeDiffusionTerm(const ChastePoint<2>& rX)
    {
        return mDiffusionTensor;
    }
};

class TestSolvingLinearPdesTutorial : public CxxTest::TestSuite
{
public:
    void TestSolvingEllipticPde() throw(Exception)
    {
        TrianglesMeshReader<2,2> mesh_reader("/people/amis080/Desktop/box.1");
        TetrahedralMesh<2,2> mesh;
        mesh.ConstructFromMeshReader(mesh_reader);

        MyPde pde;

        BoundaryConditionsContainer<2,2,1> bcc;

        bcc.DefineZeroDirichletOnMeshBoundary(&mesh); //not used in Testbox-1.hpp : This defines the boundary condition on entire boundary=0 which also includes the inner edges of the box

        ConstBoundaryCondition<2>* p_zero_boundary_condition = new ConstBoundaryCondition<2>(0.0);
        ConstBoundaryCondition<2>* p_one_boundary_condition = new ConstBoundaryCondition<2>(1.0);
        TetrahedralMesh<2,2>::BoundaryNodeIterator iter = mesh.GetBoundaryNodeIteratorBegin();
        while (iter < mesh.GetBoundaryNodeIteratorEnd())
        {
            double x = (*iter)->GetPoint()[0];
            double y = (*iter)->GetPoint()[1];
            //if (((x==0) && (y==0)) || ((x==3) && (y==0)))    //UPDATED!
            if((fabs(y-0)<1e-6))
            {
                bcc.AddDirichletBoundaryCondition(*iter, p_zero_boundary_condition);
            }

             if((fabs(x-0)<1e-6))
            {
                bcc.AddDirichletBoundaryCondition(*iter, p_zero_boundary_condition);
            }
		
	    	//if(((x==0) && (y==3)) || ((x==3) && (y==3)))    //UPDATED!
	   		if((fabs(x-3)<1e-6))
	   		{
		      bcc.AddDirichletBoundaryCondition(*iter, p_zero_boundary_condition);
	    	}

	   		if((fabs(y-3)<1e-6))
	   		{
		      bcc.AddDirichletBoundaryCondition(*iter, p_one_boundary_condition);
	    	}

            iter++;
        }

        SimpleLinearEllipticSolver<2,2> solver(&mesh, &pde, &bcc);

        Vec result = solver.Solve();

        ReplicatableVector result_repl(result);

        OutputFileHandler output_file_handler("BoxOutput");

        out_stream p_file = output_file_handler.OpenOutputFile("linear_solution.txt");

        for (unsigned i=0; i<result_repl.GetSize(); i++)
        {
            double x = mesh.GetNode(i)->rGetLocation()[0];
            double y = mesh.GetNode(i)->rGetLocation()[1];

            double u = result_repl[i];

            (*p_file) << x << " " << y << " " << u << "\n";
        }

        PetscTools::Destroy(result);
    }
};
