import matplotlib.pyplot as plt
import numpy as np
g = -9.81
v = float(input("Unesite početnu brzinu tijela: "))
if v < 0:
    print("Ponovite unos.")
else:
    theta = float(input("Unesite početni kut otklona: "))
    if theta < 0 and theta >= 360:
        print("Ponovite unos")
    else:
        theta2 = []
        x = []
        y = []
        vx = []
        vy = []
        t = []
        for i in range(1000):
            thetadva = theta*np.pi/180
            theta2.append(thetadva)
            t.append(0.01*i)
            vx.append(v*np.cos(theta2[i]))
            vy.append(v*np.sin(theta2[i]))
            y.append(vy[i]*t[i] + (g*t[i]*t[i])/2)
            x.append(vx[i]*t[i])
        plt.plot(x,y)
        plt.show()
        plt.plot(t,x)
        plt.show()
        plt.plot(t,y)
        plt.show()

