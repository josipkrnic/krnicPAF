import matplotlib.pyplot as plt
def jednoliko_gibanje(F, m):
    a0 = F/m
    dt = 0.01
    a = []
    x = []
    v = []
    t = []
    t0 = 0
    v0 = 0
    x0 = 0
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
    plt.show()
    plt.plot(t, v)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    plt.show()
    plt.plot(t, x)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Pomak [m]")
    plt.show()
jednoliko_gibanje(100, 50)
        
