import universe_moja_verzija as G
import numpy as np
import matplotlib.pyplot as plt
sunce = 1.989e30
zemlja = 5.967e24
venera = 4.869e24
merkur =3.3022e23
mars = 6.4185e23
jupiter = 1.899e27
saturn = 5.6846e26
uran = 8.681e25
neptun = 10.243e25
R = np.array((0.,0.))
aj = 1.486e11
r_zemlja = np.array((aj,0))
r_merkur = np.array((0, 0.387*aj))
r_venera = np.array((-0.722*aj,0))
r_mars = np.array((0,-1.52*aj))
r_jupiter = np.array((5.2*aj,0))
r_saturn = np.array((0,9.58*aj))
r_uran = np.array((-19.2*aj,0))
r_neptun = np.array((0,-30.1*aj))
V = np.array((0.,0.))
v_zemlja = np.array((0,29783))
v_merkur = np.array((-47861,0))
v_venera = np.array((0,-34965))
v_mars = np.array((23885,0))
v_jupiter = np.array((0, 12926))
v_saturn = np.array((-9619,0))
v_uran = np.array((0,6790))
v_neptun = np.array((5420,0))
sz = G.Gravitacija()
smerk = G.Gravitacija()
sv = G.Gravitacija()
smars = G.Gravitacija()
sjup = G.Gravitacija()
ssat = G.Gravitacija()
suran = G.Gravitacija()
snep = G.Gravitacija()
sz.init(sunce,zemlja,R,r_zemlja,V,v_zemlja)
smerk.init(sunce,merkur,R,r_merkur,V,v_merkur)
sv.init(sunce,venera,R,r_venera,V,v_venera)
smars.init(sunce,mars,R,r_mars,V,v_mars)
sjup.init(sunce,jupiter,R,r_jupiter,V,v_jupiter)
ssat.init(sunce,saturn,R,r_saturn,V,v_saturn)
suran.init(sunce,uran,R,r_uran,V,v_uran)
snep.init(sunce,neptun,R,r_neptun,V,v_neptun)
T_zemlja = 60*60*24*365
T_merkur = 0.2409*T_zemlja
T_venera = 0.616*T_zemlja
T_mars = 1.9*T_zemlja
T_jupiter = 12*T_zemlja
T_saturn = 29.5*T_zemlja
T_uran = 84*T_zemlja
T_neptun = 165*T_zemlja
X,Y,x,y = sz.move(T_zemlja)
X1,Y1,x1,y1 = smerk.move(T_merkur)
X2,Y2,x2,y2 = sv.move(T_venera)
X3,Y3,x3,y3 = smars.move(T_mars)
X4,Y4,x4,y4 = sjup.move(T_jupiter)
X5,Y5,x5,y5 = ssat.move(T_saturn)
X6,Y6,x6,y6 = suran.move(T_uran)
X7,Y7,x7,y7 = snep.move(T_neptun)
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(X,Y,"yo",label="Sunce")
plt.plot(x1,y1,"green",label="Merkur")
plt.plot(x2,y2,"gold",label="Venera")
plt.plot(x,y,"blue",label="Zemlja")
plt.plot(x3,y3,"red",label="Mars")
plt.plot(x4,y4,"white",label="Jupiter")
plt.plot(x5,y5,"brown",label="Saturn")
plt.plot(x6,y6,"lightsteelblue",label="Uran")
plt.plot(x7,y7,"darkblue", label="Neptun")
plt.legend(loc="best")
plt.savefig("suncev_sustav_krnic_edition.pdf")
plt.show()
