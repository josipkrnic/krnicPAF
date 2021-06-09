import Gravitacija as G
import numpy as np
import matplotlib.pyplot as plt
sunce = 1.989e30
zemlja = 5.967e24
R = np.array((0.,0.))
aj = 1.486e11
r = np.array((aj,0))
V = np.array((0.,0.))
v = np.array((0,29783))
sz = G.Gravitacija()
sz.init(sunce,zemlja,R,r,V,v)
T = 60*60*24*365
X,Y,x,y = sz.move(T)
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(X,Y,color="yellow")
plt.plot(x,y,"blue")
plt.show()
