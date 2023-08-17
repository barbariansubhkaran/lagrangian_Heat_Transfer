from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.RunDictionary.LagrangianCloudData import LagrangianCloudData
import pandas as pd
sol = SolutionDirectory(".")
data = pd.concat([LagrangianCloudData(".","reactingCloud1",t).data for t in sol.times if float(t) > 0])
data = data.round({'Px': 4, 'Py': 4, 'Pz': 4})
data.to_csv("lagrangian.csv")

