# ----------------------------------------------------------------------------- 
# Project      : OSCFD 2022
# 
# Name         : createReactingCloud1Positions.py
#
# Prepared     : Orjan Fjallborg LKAB
#
# Description  : Creates the file reactingCloud1Positions
#
# History      : 
# 1, 2022-12-07, klorfj, Created
# ----------------------------------------------------------------------------- 
import io
from string import Template
import os

# -----------------------------------------------------------------------------
# Name:         createPositions
# Summary:      creates the positions assuming rectangular and uniformly 
#               sized cells in the mesh
# Returns:      see above
# -----------------------------------------------------------------------------
def createPositions():
    buf = io.StringIO()

    Nx, Ny, Nz = (50, 1, 1)       # no of cells in x- y- and z direction
    min = [4, 0, 0]                # min coordinate of bounding box
    max = [4.5, 1, 1]              # max coordinate of bounding box
    cs_x = (max[0] - min[0]) / Nx
    cs_y = (max[1] - min[1]) / Ny
    cs_z = (max[2] - min[2]) / Nz

    for k in range(Nz):
        z = cs_z / 2 + k * cs_z + min[2]   
        for j in range(Ny):
            y = cs_y / 2 + j * cs_y + min[1]
            for i in range(Nx):
                x = cs_x / 2 + i * cs_x + min[0]
                buf.write('    ({0} {1} {2})\n'.format(x, y, z))
    
    return buf.getvalue()

# -----------------------------------------------------------------------------
# Name:         createContent
# Summary:      Creates the position vector field as a string
# Returns:      see above
# -----------------------------------------------------------------------------
def createContent():
    template = Template(r'''/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2112                                 |
|   \\  /    A nd           | Web:      www.openfoam.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       vectorField;
    object      reactingCloud1Positions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
(
$internalField
)
// ************************************************************************* //
''')

    return template.substitute(
        internalField = createPositions()
    )




f = open(os.getcwd() + "/constant/reactingCloud1Positions", 'w')
f.write(createContent())
f.close()
