import matplotlib.pyplot as plt
import math
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
    plt.show()
    plt.plot(t,y)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("y [m]")
    plt.show()
    plt.plot(t,v)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    plt.show()
    plt.plot(x,y)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()
kosi_hitac(50, 60, 0, 0)
        
    
