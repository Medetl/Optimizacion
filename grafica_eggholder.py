import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-512, 512, 10)
Y = np.arange(-512, 512, 10)
X, Y = np.meshgrid(X, Y)

Z = (-(Y + 47.0) * np.sin(np.sqrt(abs(X/2.0 + (Y + 47.0)))) - X * np.sin(np.sqrt(abs(X - (Y + 47.0)))))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(-1000, 1000)

pl.show()