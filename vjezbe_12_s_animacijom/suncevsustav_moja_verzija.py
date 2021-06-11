import universe_moja_verzija as G
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sunce = 1.989e30
zemlja = 5.967e24
venera = 4.869e24
merkur =3.3022e23
mars = 6.4185e23
R = np.array((0,0))
aj = 1.486e11
r_zemlja = np.array((aj,0))
r_merkur = np.array((0, 0.387*aj))
r_venera = np.array((-0.722*aj,0))
r_mars = np.array((0,-1.52*aj))
V = np.array((0,0))
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
fig = plt.figure("Sunčev sustav", figsize=(15,15))
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(X,Y,"yo",label="Sunce")
plt.plot(x1,y1,"green",label="Merkur")
plt.plot(x2,y2,"gold",label="Venera")
plt.plot(x,y,"blue",label="Zemlja")
plt.plot(x3,y3,"red",label="Mars")
plt.legend(loc="best")
animmerkur, = plt.plot([0],[0.387*aj],"go")
animvenera, = plt.plot([-0.722*aj],[0],"yo")
animzemlja, = plt.plot([aj],[0],"bo")
animmars, = plt.plot([0],[-1.52*aj],"ro")
def init_merkur():
    animmerkur.set_data([],[])
    return animmerkur,
def init_venera():
    animvenera.set_data([],[])
    return animvenera,
def init_zemlja():
    animzemlja.set_data([],[])
    return animzemlja,
def init_mars():
    animmars.set_data([],[])
    return animmars,
def animate_merkur(i):
    xmerkur = x1[i]
    ymerkur = y1[i]
    animmerkur.set_data(xmerkur,ymerkur)
    return animmerkur,
def animate_venera(i):
    xvenera = x2[i]
    yvenera = y2[i]
    animvenera.set_data(xvenera,yvenera)
    return animvenera,
def animate_zemlja(i):
    xzemlja = x[i]
    yzemlja = y[i]
    animzemlja.set_data(xzemlja,yzemlja)
    return animzemlja,
def animate_mars(i):
    xmars = x3[i]
    ymars = y3[i]
    animmars.set_data(xmars,ymars)
    return animmars,
myAnimation1 = animation.FuncAnimation(fig,animate_merkur,frames=88,init_func=init_merkur,interval=50,blit=True)
myAnimation2 = animation.FuncAnimation(fig,animate_venera,frames=224,init_func=init_venera,interval=40,blit=True)
myAnimation3 = animation.FuncAnimation(fig,animate_zemlja,frames=365,init_func=init_zemlja,interval=25,blit=True)
myAnimation4 = animation.FuncAnimation(fig,animate_mars,frames=686,init_func=init_mars,interval=10,blit=True)
plt.show()

