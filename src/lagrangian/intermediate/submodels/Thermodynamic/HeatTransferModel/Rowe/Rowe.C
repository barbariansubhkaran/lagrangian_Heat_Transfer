/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2011 OpenFOAM Foundation
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

\*---------------------------------------------------------------------------*/

#include "Rowe.H"

// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

template<class CloudType>
Foam::Rowe<CloudType>::Rowe
(
    const dictionary& dict,
    CloudType& cloud
)
:
    HeatTransferModel<CloudType>(dict, cloud, typeName),
    vo_(this->coeffDict().template get<scalar>("vo"))
{}


template<class CloudType>
Foam::Rowe<CloudType>::Rowe(const Rowe<CloudType>& htm)
:
    HeatTransferModel<CloudType>(htm),
    vo_(htm.vo_)
{}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

template<class CloudType>
Foam::scalar Foam::Rowe<CloudType>::Nu
(
    const scalar Re,
    const scalar Pr
) const
{
    const scalar a = 2 / (1 - cbrt(1 - vo_));
    const scalar b = 2 / (3 * vo_);    
    const scalar m = 2.0 / 3.0;
    scalar n = 1.0 / 3.0;
    if (Re != 0) {
        const scalar R_hat = 4.65 * pow(Re, -0.28);
        n = (2 + R_hat) / (3 * R_hat + 3);
    }
    const scalar Nu = a + b * pow(Re, n) * pow(Pr, m);

    if (debug)
    {        
        Info << "-----------------------" << nl
            << "Re       = " << Re << nl
            << "Pr       = " << Pr << nl
            << "vo       = " << vo_ << nl
            << "a        = " << a << nl
            << "b        = " << b << nl
            << "m        = " << m << nl
            << "n        = " << n << nl
            << "Nu       = " << Nu << nl
            << endl;
    }
    return Nu;
}


// ************************************************************************* //
