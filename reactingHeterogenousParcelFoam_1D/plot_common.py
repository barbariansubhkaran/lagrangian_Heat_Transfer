# ----------------------------------------------------------------------------- 
# Project      : OSCFD 2022
# 
# Name         : plot_common.py
#
# Prepared     : Orjan Fjallborg LKAB
#
# Description  : Global parameters and plot functionality.
#
# History      : 
# 1, 2022-12-07, klorfj, Created
# ----------------------------------------------------------------------------- 
import numpy as np
import os, sys
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import datetime
from PlotData import PlotData

# Global parameters

PLOT_DATA_ARR = [
    PlotData(color='black', line_style='solid', text='Ranz-Marshall', case='rectangularDuct1'),
    PlotData(color='blue', line_style='dashed', text='Rowe', case='rectangularDuct2'),
    PlotData(color='black', line_style='solid', text='Rowe', case='rectangularDuct3'),
    PlotData(color='blue', line_style='dashed', text='Rowe HR int', case='rectangularDuct4')
]



# -----------------------------------------------------------------------------
# Name:         plot_array
# Summary:      Plotts x- and y- data arrays to the Axes ax.
# Params:       ax      (I/O) - Axes object
#               xa        (I) - x data array
#               ya        (I) - y data array
#               pd        (I) - a PlotData object
#               add_label (I) - Set label if True
# -----------------------------------------------------------------------------
def plot_array(ax, xa, ya, pd, add_label=False):
    
    if (add_label):
        ax.plot(xa, ya, color=pd.color, linewidth=1, linestyle=pd.line_style,
            label = pd.text)
    else:
        ax.plot(xa, ya, color=pd.color, linewidth=1, linestyle=pd.line_style)

# -----------------------------------------------------------------------------
# Name:         plot_array_exp
# Summary:      Plotts x- and y- experimental data arrays to the Axes ax.
# Params:       ax      (I/O) - Axes object
#               xa        (I) - x data array
#               ya        (I) - y data array
#               add_label (I) - Set label if True
# -----------------------------------------------------------------------------
def plot_array_exp(ax, xa, ya, add_label=False):
    
    if (add_label):
        ax.plot(xa, ya, linestyle='none', marker='o', fillstyle='none', 
            markersize=3, markeredgecolor = 'b',
            label = "Experiment")
    else:
        ax.plot(xa, ya, linestyle='none', marker='o', fillstyle='none', 
            markersize=3, markeredgecolor = 'b', linewidth=1)
