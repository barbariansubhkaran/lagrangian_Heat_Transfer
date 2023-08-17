# ----------------------------------------------------------------------------- 
# Project      : OSCFD 2022
# 
# Name         : plot_lagrangian_layers_T_chem.py
#
# Prepared     : Orjan Fjallborg LKAB
#
# Description  : Plots the temperature from LPT data for heat transfer model comparison. 
#                One subplot is created for each position in x.
#
# History      : 
# 1, 2022-12-18, klorfj, Created
# ----------------------------------------------------------------------------- 
import pandas as ps
import numpy as np
import os, sys
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import datetime
import plot_common as pc
from PlotData import PlotData

# -----------------------------------------------------------------------------
# Name:         add_sim_T_to_plot
# Summary:      queries the LPT data and adds temperature to the Axes ax.
# Params:       ax      (I/O) - Axes object
#               x_layer   (I) - x layer
#               data      (I) - PyFoam LPT pandas data
#               pd        (I) - a PlotData object
#               add_label (I) - Set label if True
# -----------------------------------------------------------------------------
def add_sim_T_to_plot(ax, x_layer, data, pd, add_label=False):
    xa=[]
    ya=[]

    ds = 0.005

    query = (
        'Px >= ' + str(x_layer) + ' - ' + str(ds) + ' and '
        'Px <= ' + str(x_layer) + ' + ' + str(ds)
        )
    data.query(query, inplace=True)
        
    grouped = data.groupby(["age"])
    avg = grouped.aggregate(np.average)

    xa = data['age'].apply(np.array).unique()
    ya = avg['T'].values-273

    pc.plot_array(ax, xa, ya, pd, add_label)



fig = plt.figure(figsize=(12, 16))
gs = fig.add_gridspec(3, 2, hspace=0.5)
axs = gs.subplots()
ax_ix = 0
for x_layer in [4.05, 4.15, 4.25, 4.35, 4.45]:
    ax = axs[math.floor(ax_ix / 2), ax_ix % 2]
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_xmargin(0)
    ax.set_ymargin(0)
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.tick_params(top=True, right=True)
    ax.tick_params(which = 'major', top = True, right = True)
    ax.tick_params(which = 'minor', top = True, right = True)
    dir = os.getcwd()

    data1 = ps.read_csv(dir + "/lagrangian3.csv")
    data2 = ps.read_csv(dir + "/lagrangian4.csv")
    add_sim_T_to_plot(ax, x_layer, data1, pc.PLOT_DATA_ARR[2], True)
    add_sim_T_to_plot(ax, x_layer, data2, pc.PLOT_DATA_ARR[3], True)

    ax.set_xlabel("$t \; (s)$")
    ax.set_ylabel("$T \; (^{\circ} C)$")
    ax.set_title("Average temperature at x = " + str(x_layer) + " m")
    ax.legend(loc="lower right")
    ax_ix = ax_ix + 1


# Plot for all positions in the last subplot
ax = axs[2, 1]
txt1 = pc.PLOT_DATA_ARR[0].text
txt2 = pc.PLOT_DATA_ARR[1].text
for x_layer in [4.05, 4.15, 4.25, 4.35, 4.45]:
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_xmargin(0)
    ax.set_ymargin(0)
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.tick_params(top=True, right=True)
    ax.tick_params(which = 'major', top = True, right = True)
    ax.tick_params(which = 'minor', top = True, right = True)
    dir = os.getcwd()

    data1 = ps.read_csv(dir + "/lagrangian3.csv")
    data2 = ps.read_csv(dir + "/lagrangian4.csv")
    pc.PLOT_DATA_ARR[0].text = txt1 + " " + str(x_layer)
    pc.PLOT_DATA_ARR[1].text = txt2 + " " + str(x_layer)
    add_sim_T_to_plot(ax, x_layer, data1, pc.PLOT_DATA_ARR[2], True)
    add_sim_T_to_plot(ax, x_layer, data2, pc.PLOT_DATA_ARR[3], True)

    ax.set_xlabel("$t \; (s)$")
    ax.set_ylabel("$T \; (^{\circ} C)$")
    ax.set_title("Average temperature")
    ax.legend(loc="lower right")

plt.savefig("plot_lagrangian_layers_T_chem.eps")
plt.savefig("plot_lagrangian_layers_T_chem.png")
