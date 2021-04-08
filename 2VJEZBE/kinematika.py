import numpy as np 
import matplotlib.pyplot as plt
import math
g = -9.81
def jednoliko_gibanje(F,m,v0,x0):
    while True:
        F = float(input("Unesite silu kod jednolikog gibanja: "))
        m = float(input("Unesite masu objekta kod jednolikog gibanja: "))
        if m < 0:
            print("Ponovite unos.")
        else:
            v0 = float(input("Unesite početnu brzinu kod jednolikog gibanja: "))
            x0 = float(input("Unesite počeetni položaj tijela kod jednolikog gibanja: "))
            a = []
            x = []
            v = []
            t = []
            for i in range(1000):
                t.append(0.01*i)
                a.append(F/m)
                v.append(v0 + a[i]*t[i])
                x.append((v[i]*t[i])/2)
            plt.plot(t,x)
            plt.show()
            plt.plot(t,v)
            plt.show()
            plt.plot(t,a)
            plt.show()
def kosi_hitac(v0,theta):
    while True:
        v = float(input("Unesite početnu brzinu tijela: "))
        if v < 0:
            print("Ponovite unos.")
        else:
            theta = float(input("Unesite početni kut otklona: "))
            if theta < 0 and theta >= 360:
                print("Ponovite unos")
            else:
                vx = []
                vy = []
                t = []
                x = []
                y = []
                theta2 = []
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

