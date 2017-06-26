# PVWatts Tool
### Author: Will Arnuk
#### Date: 6-26-17
###### Version: 0.1.dev
###### Credits: NREL
###### Requirements: pandas, requests, PyQt5

PVWatts_Tool is based off of NREL APIs, including the PVWatts (v5) API and the Energy Utilities API.

It allows a user to input a variety of parameters and quickly get useful information on AC potential from solar. Annual output is provided, as well as ratios for annual kWh per sq. meter and daily ratios for peak, low, and median days. Additionally, local energy utilties and rates are used to calculate the value of the annual potential from solar. 

_____

The GUI tool can be run from the python interpreter using the following commands:

    import PVWatts_Tool
    PVWatts_Tool.run()

This launches the GUI, built using PyQt5. Input parameters are entered in the left pane, output is printed to the right.
