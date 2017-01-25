This file include two subfolders:
1) **data** - containing .node, .edge, .ele file of the box geometry downloaded from [Triangle 
A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator](https://people.sc.fsu.edu/~jburkardt/c_src/triangle/triangle.html)

2) **chaste** - containing code written using the chaste framework to execute the Laplacian equation on the box geometry providing
...gradient 1 and 0 on opposite side of the box and the visualisation of the gradients on the geometry.


To run any of these hpp file, call from the main chaste directory:
scons build=GccDebug_warn test_suite=./projects/example/test/<your file>/<filename>.hpp 
