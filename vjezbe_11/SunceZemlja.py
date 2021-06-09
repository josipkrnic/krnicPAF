import Gravitacija as G
import numpy as np
import matplotlib.pyplot as plt
sunce = 2e30
zemlja = 6e24
R = np.array((0,0))
aj = 1.486e11
r = np.array((aj,0))
V = np.array((0,0))
v = np.array((0,29783))
sz = G.Gravitacija(sunce,zemlja,R,r,V,v)
T = 60*60*24*365
X,x,Y,y = sz.move(T)
plt.plot(X,Y)
plt.plot(x,y)
plt.show()
