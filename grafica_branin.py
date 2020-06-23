###################################################################################################
###																								
###		Funcion RCOS de Branin:																	
###		f(x,y)=a(y-bx^2+cx-d)^2 + e(1-f)cos(x) + e 												
###		Rangos:    -5<= x <=10; 0<=y<=15     													
###		Con a=1, b=5.1/(4pi^2), c=5/pi, d=6, e=10, f=1/(8pi)   									
###		Tiene minimo global f(x,y)=0.397887 en (-pi,12.275), (pi, 2.275) y (9.42478, 2.475)  	
###																								
###################################################################################################


import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-5, 10, 0.5)
Y = np.arange(0, 15, 0.5)
X, Y = np.meshgrid(X, Y)

Z = (Y - 5.1/(4*np.pi**2)*X**2 + (5.0/np.pi)*X - 6)**2 + 10.0*(1 - 1.0/(8*np.pi))*np.cos(X) + 10

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(0, 300)

pl.show()