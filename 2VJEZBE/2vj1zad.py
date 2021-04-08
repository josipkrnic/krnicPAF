import matplotlib.pyplot as plt
import numpy as np
while True:    
    F = float(input("Unesite iznos sile: "))
    if F < 0:
        print("Ponovite unos.")
    else:
        m = float(input("Unesite masu tijela: "))
        if m < 0:
            print("Ponovite unos.")
        else:
            t = []
            x = []
            v = []
            a = []
            for i in range(1000):
                t.append(0.01*i)
                a.append(F/m)
                v.append(a[i]*t[i])
                x.append(v[i]*t[i]*0.5)
            plt.plot(t,x)
            plt.show()
            plt.plot(t,v)
            plt.show()
            plt.plot(t,a)
            plt.show() 