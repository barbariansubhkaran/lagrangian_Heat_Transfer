/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2011-2016 OpenFOAM Foundation
    Copyright (C) 2021 OpenCFD Ltd.
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Class
    Foam::Rowe

Group
    grpLagrangianIntermediateHeatTransferSubModels

Description
    Nusselt-number model using the empirical Rowe correlation
    to be used in modelling of the fluid-particle heat transfer coefficient:

    \f[
        \mathrm{Nu} = A + B\mathrm{Re}^n\mathrm{Pr}^{2/3}
    \f]
    with

    \f[
        \mathrm{Re} =
            \frac{\rho_c \, | \mathbf{u}_\mathrm{rel} | \, d_p}{\mu_c}
    \f]
	with
	
    \f[
        A = \frac{2}{1 - (1 - \epsilon_\mathrm{v})^{1/3}}
    \f]
	
    \f[
	    B = \frac{2}{3\epsilon_\mathrm{v}}
    \f]

    \f[
        \frac{2 - 3n}{3n-1} = 4.65\mathrm{Re}^{-0.28}
    \f]

    \f[
        \mathrm{Pr} = \frac{ C_p \, \mu_c }{ \kappa_c }
    \f]
    where

    \vartable
        \mathrm{Nu}    | Nusselt number
        \mathrm{Re}    | Reynolds number
        \mathrm{Pr}    | Prandtl number
        d_p            | Particle diameter
        \rho_c         | Density of carrier in the film surrounding particle
        \mu_c    | Dynamic viscosity of carrier in the film surrounding particle
        \mathbf{u}_\mathrm{rel} | Relative velocity between particle and carrier
        \epsilon_\mathrm{v} | Bed voidage
        C_p            | Specific heat capacity
        \kappa_c       | Thermal conductivity of carrier in the film
    \endvartable

    Reference:
    \verbatim
        Standard model:
            P. N. Rowe, K. T. Claxton and J. B. Lewis (1965)
            Heat and mass transfer from a single sphere in an extensive flowing fluid.
            Transaction of Institute Chemical Engineering, 43, pp. 14-31.

    \endverbatim

Usage
    Minimal example by using \c constant/\<CloudProperties\>:
    \verbatim
    subModels
    {
        // Mandatory entries
        heatTransferModel    Rowe;

        // Optional entries
        RoweCoeffs
        {
            vo    0.3;
        }
    }
    \endverbatim

    where the entries mean:
    \table
      Property           | Description              | Type | Reqd | Deflt
      heatTransferModel  | Type name: Rowe  | word | yes  | -
      vo                 | Bed voidage  | scalar | yes | -
    \endtable

SourceFiles
    Rowe.C

\*---------------------------------------------------------------------------*/

#ifndef Rowe_H
#define Rowe_H

#include "HeatTransferModel.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

/*---------------------------------------------------------------------------*\
                         Class Rowe Declaration
\*---------------------------------------------------------------------------*/

template<class CloudType>
class Rowe
:
    public HeatTransferModel<CloudType>
{
    // Private Data

        //- Voidage
        const scalar vo_;


public:

    //- Runtime type information
    TypeName("Rowe");


    // Generated Methods

        //- No copy assignment
        void operator=(const Rowe&) = delete;


    // Constructors

        //- Construct from dictionary
        Rowe(const dictionary& dict, CloudType& cloud);

        //- Copy construct
        Rowe(const Rowe<CloudType>& im);

        //- Construct and return a clone
        virtual autoPtr<HeatTransferModel<CloudType>> clone() const
        {
            return autoPtr<HeatTransferModel<CloudType>>
            (
                new Rowe<CloudType>(*this)
            );
        }


    //- Destructor
    virtual ~Rowe() = default;


    // Member Functions

        // Evaluation

            //- Return Nusselt number
            virtual scalar Nu
            (
                const scalar Re,
                const scalar Pr
            ) const;
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#ifdef NoRepository
    #include "Rowe.C"
#endif

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //
