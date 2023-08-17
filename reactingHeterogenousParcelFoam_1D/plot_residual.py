import matplotlib.pyplot as plt
import numpy as np
import os, sys

fig = plt.figure()
ax = plt.axes()
ax.set_yscale('log')
ax.set_xlim(0, 5)

dir = os.getcwd() + "/rectangularDuct2/logs/"

def add_residual_to_plot(ax, dir, residual):
    xa=[]
    ya=[]

    #for residual in os.listdir(dir):

    filePath = dir + "/" + residual
    abc = np.loadtxt(filePath, skiprows=1)
    for row in abc:
        x = row[0]
        xa.append(x)
        y = row[1]
        ya.append(y)
    
    ax.plot(xa, ya, label = residual)

add_residual_to_plot(ax, dir, "rhoFinalRes_2")
add_residual_to_plot(ax, dir, "UxFinalRes_0")
add_residual_to_plot(ax, dir, "p_rghFinalRes_1")
add_residual_to_plot(ax, dir, "hFinalRes_0")
add_residual_to_plot(ax, dir, "O2FinalRes_0")
#add_residual_to_plot(ax, dir, "CourantMax_0")

#CourantMax_0   O2_0          clockTime_0       contLocal_1      h_0              p_rgh_1        rhoIters_2
#CourantMax_1   Separator_0   contCumulative_0  deltaT_0         p_rghFinalRes_0  rhoFinalRes_0  rho_0
#CourantMean_0  Time_0        contCumulative_1  executionTime_0  p_rghFinalRes_1  rhoFinalRes_1  rho_1
#CourantMean_1  UxFinalRes_0  contGlobal_0      foamLog.awk      p_rghIters_0     rhoFinalRes_2  rho_2
#O2FinalRes_0   UxIters_0     contGlobal_1      hFinalRes_0      p_rghIters_1     rhoIters_0
#O2Iters_0      Ux_0          contLocal_0       hIters_0         p_rgh_0          rhoIters_1

ax.legend(loc="upper right")
plt.show()