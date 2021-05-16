import matplotlib.pyplot as plt
import math
def jednoliko_gibanje(F, m, v0, x0):
    a0 = F/m
    dt = 0.01
    a = []
    x = []
    v = []
    t = []
    t0 = 0
    for i in range(0,1000):
        a.append(a0)
        t0 = dt*i
        t.append(t0)
        v0 += a0*dt
        v.append(v0)
        x0 += v0*dt
        x.append(x0)
    plt.plot(t, a)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Akceleracija [m/s^2]")
    plt.title("Jednoliko gibanje - a,t graf")
    plt.show()
    plt.plot(t, v)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    plt.title("Jednoliko gibanje - v,t graf")
    plt.show()
    plt.plot(t, x)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Pomak [m]")
    plt.title("Jednoliko gibanje - x,t graf")
    plt.show()
def kosi_hitac(v0, theta, x0, y0):
    dt = 0.01
    v0_x = v0*math.cos(math.radians(theta))
    v0_y = v0*math.sin(math.radians(theta))
    v0x = []
    v0y = []
    v = []
    t0 = 0
    t = []
    x = []
    y = []
    for i in range(0,1000):
        t0 = dt*i
        t.append(t0)
        v0x.append(v0_x)
        v0_y = v0_y - 9.81*dt
        v0y.append(v0_y)
        brzina = math.sqrt(v0_x**2 + v0_y**2)
        v.append(brzina)
        x0 = x0 + v0_x*dt
        x.append(x0)
        y0 = y0 + v0_y*dt
        y.append(y0)
    plt.plot(t,x)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("x [m]")
    plt.title("Kosi hitac - x,t graf")
    plt.show()
    plt.plot(t,y)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("y [m]")
    plt.title("Kosi hitac - y,t graf")
    plt.show()
    plt.plot(t,v)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    plt.title("Kosi hitac - v,t graf")
    plt.show()
    plt.plot(x,y)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Kosi hitac - x,y graf")
    plt.show()

        
