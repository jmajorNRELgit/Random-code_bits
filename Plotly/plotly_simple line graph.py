# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:22:05 2019

@author: jmajor
"""

from plotly.offline import plot

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 5
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

plot(data, filename='basic-line')