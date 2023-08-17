/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2018-2019 OpenCFD Ltd.
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
    Foam::basicMyHeterogeneousReactingParcel

Description
    Definition of reacting heterogeneous parcel

SourceFiles
    basicMyHeterogeneousReactingParcel.C

\*---------------------------------------------------------------------------*/

#ifndef basicMyHeterogeneousReactingParcel_H
#define basicMyHeterogeneousReactingParcel_H

#include "contiguous.H"
#include "particle.H"
#include "KinematicParcel.H"
#include "MyThermoParcel.H"
#include "ReactingParcel.H"
#include "ReactingHeterogeneousParcel.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{
    typedef ReactingHeterogeneousParcel
    <
        ReactingParcel
        <
            MyThermoParcel
            <
                KinematicParcel
                <
                    particle
                >
            >
        >
    > basicMyHeterogeneousReactingParcel;

    //- Non-contiguous data for basicMyHeterogeneousReactingParcel
    template<>
    struct is_contiguous<basicMyHeterogeneousReactingParcel> : std::false_type {};
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //
