# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:48:30 2019

@author: jmajor
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import pandas as pd
import numpy as np
from scipy import signal

#calibration
file = 'C:/Users/jmajor/Desktop/Fast_charge_part_2/Condensed data.csv'



calibration_slope =  7.89768885939907
calibration_intercept = -0.0005410827748427023


df = pd.read_csv(file)

#data from calibration
TEG1 = df['TEG1']
TEG2 = df['TEG2']
current = df['Current']
supply_voltage = df['Supply_voltage']
cell_voltage = df['Cell_voltage']
time = df['Time']

TEG_sum = []
for i in range(len(TEG1)):
    TEG_sum.append(TEG1[i] + TEG2[i])

TEG_fitted = [(i*calibration_slope+calibration_intercept) for i in TEG_sum]





power = []
for i in range(len(supply_voltage)):
    power.append(supply_voltage[i] * current[i])


x = time
TEG_fitted = [i*1000 for i in TEG_fitted]
power = [i*1000 for i in power]

fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))
#ax1.set(facecolor='#FFFFCC')



ax1.plot(x, TEG_fitted, label = 'Fitted TEG data')
ax1.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
ax1.set_title('Press left mouse button and drag to test')

ax1.plot(x, power, label = 'Supply Power')
ax1.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Power (mWatts)')

ax2.plot(x, TEG_fitted, label = 'Fitted TEG data')
ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
ax2.set_title('Press left mouse button and drag to test')

ax2.plot(x, power, label = 'Supply Power')
ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))

ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Power (mWatts)')


'''change TEG data to charge power data'''
#TEG_fitted = power


def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    ax2.clear()
    ax2.plot(x[indmin:indmax], TEG_fitted[indmin:indmax], label = 'Fitted TEG data')
    ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
    ax2.set_title('Press left mouse button and drag to test')

    ax2.plot(x[indmin:indmax], power[indmin:indmax], label = 'Supply Power')
    ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
    fig.canvas.draw()

# Set useblit=True on most backends for enhanced performance.
span = SpanSelector(ax1, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))



#data collected from the plot
data_lists = []


def onselect2(xmin, xmax):
    global data_dictionaries
    x_data = None

    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    x_data = x[indmin:indmax]
    TEG_data_to_integrate = TEG_fitted[indmin:indmax]

    integration_time = time[indmin:indmax]


    data_lists.append((x_data, TEG_data_to_integrate, integration_time))

    # Set useblit=True on most backends for enhanced performance.
span2 = SpanSelector(ax2, onselect2, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))


plt.show(block = True)

for i in range(len(data_lists)):
    plt.fill_between(data_lists[i][2],[0]*len(data_lists[i][0]), data_lists[i][1])

for i in range(len(data_lists)):
    print('{}'.format( np.abs(np.trapz(data_lists[i][1]))))