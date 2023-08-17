# ----------------------------------------------------------------------------- 
# Project      : OSCFD 2022
# 
# Name         : PlotData.py
#
# Prepared     : Orjan Fjallborg LKAB
#
# Description  : Class handling data for different case trends in the same plot
#
# History      : 
# 1, 2022-12-07, klorfj, Created
# ----------------------------------------------------------------------------- 

class PlotData(object):
    # -----------------------------------------------------------------------------
    # Name:         __init__
    # Summary:      Constructor
    # Params:       
    # Returns:      the contructed object
    # -----------------------------------------------------------------------------
    def __init__(self, color, line_style, text, case):
        self.color = color
        self.line_style = line_style
        self.text = text
        self.case = case
    
    