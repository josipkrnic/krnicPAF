import universe_moja_verzija as G
import numpy as np
import matplotlib.pyplot as plt
sunce = 1.989e30
zemlja = 5.967e24
venera = 4.869e24
merkur =3.3022e23
mars = 6.4185e23
R = np.array((0.,0.))
aj = 1.486e11
r_zemlja = np.array((aj,0))
r_merkur = np.array((0, 0.387*aj))
r_venera = np.array((-0.722*aj,0))
r_mars = np.array((0,-1.52*aj))
V = np.array((0.,0.))
v_zemlja = np.array((0,29783))
v_merkur = np.array((-47861,0))
v_venera = np.array((0,-34965))
v_mars = np.array((23885,0))
sz = G.Gravitacija()
smerk = G.Gravitacija()
sv = G.Gravitacija()
smars = G.Gravitacija()
sz.init(sunce,zemlja,R,r_zemlja,V,v_zemlja)
smerk.init(sunce,merkur,R,r_merkur,V,v_merkur)
sv.init(sunce,venera,R,r_venera,V,v_venera)
smars.init(sunce,mars,R,r_mars,V,v_mars)
T_zemlja = 60*60*24*365
T_merkur = 0.2409*T_zemlja
T_venera = 0.616*T_zemlja
T_mars = 1.9*T_zemlja
X,Y,x,y = sz.move(T_zemlja)
X1,Y1,x1,y1 = smerk.move(T_merkur)
X2,Y2,x2,y2 = sv.move(T_venera)
X3,Y3,x3,y3 = smars.move(T_mars)
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(X,Y,"yo",label="Sunce")
plt.plot(x1,y1,"green",label="Merkur")
plt.plot(x2,y2,"gold",label="Venera")
plt.plot(x,y,"blue",label="Zemlja")
plt.plot(x3,y3,"red",label="Mars")
plt.legend(loc="best")
plt.show()
