# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:49:12 2019

@author: jmajor
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import numpy as np


x = [1,2,3,4,5,6,7,8,9,10]
y = [34,65,23,87,63,76,98,43,12,67]

fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))

ax1.plot(x,y)
ax2.plot(x,y)


def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)
    print('X min and max: ',indmin, indmax)
    ax2.clear()
    ax2.plot(x[indmin:indmax], y[indmin:indmax])
    plt.show()


# Set useblit=True on most backends for enhanced performance.
span = SpanSelector(ax1, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))


plt.show(block = True)
print('Done')