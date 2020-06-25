###################################################################################################
###																								
###		Primera función de De Jong:																	
###		f(x,y)=x^2 + y^2 												
###		Rangos:    -5.12<= x <=5.12; -5.12<= y <=5.12    													
###		   									
###		Tiene minimo global f(x,y)=0 en (0,0)  	
###																								
###################################################################################################

import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-5.12, 5.12, 0.2)
Y = np.arange(-5.12, 5.12, 0.2)
X, Y = np.meshgrid(X, Y)
Z = X ** 2 + Y ** 2

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(0, 50)

pl.show()