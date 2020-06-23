import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-5, 15, 1)
Y = np.arange(-5, 15, 1)
X, Y = np.meshgrid(X, Y)

Z = (Y - 5.1/(4*np.pi**2)*X**2 + (5.0/np.pi)*X - 6)**2 + 10.0*(1 - 1.0/(8*np.pi))*np.cos(X) + 10

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(0, 300)

pl.show()