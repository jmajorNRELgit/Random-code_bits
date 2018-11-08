import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# The following import is necessary to enable 3D plots in matplotlib.
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



data = pd.read_excel('xenon.xlsx')

x = list(map(float,data.columns.values))
y = list(map(float,data.index.values))


X,Y = np.meshgrid(x,y)
Z = data

fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')

surf = ax.plot_surface(X,Y,Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
