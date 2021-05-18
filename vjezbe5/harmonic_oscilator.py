import matplotlib.pyplot as plt
import math
class HarmonicOscilator:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
    def init(self, x0, v0, masa = 1, konstanta = 20, faza0 = 0, dt = 0.01):
        self.t.append(0)
        self.x0 = x0
        self.x.append(self.x0)
        self.v.append(v0)
        self.m = masa
        self.k = konstanta
        self.fi = faza0
        self.omega = -self.k/self.m
        self.a.append((self.omega*self.x0))
        self.dt = dt
    def reset(self):
        self.t.clear()
        self.x.clear()
        self.v.clear()
        self.a.clear()
    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a.append(self.omega*self.x[i-1])
        self.v.append(self.v[i-1] + self.a[i]*self.dt)
        self.x.append(self.x[i-1] + self.v[i]*self.dt)
    def titranje(self, t_):
        i_ = t_/self.dt
        i_round = int(i_)
        for i in range(1, i_round):
            self.__move(i)
        return self.x, self.t, self.v, self.a
    def analiticki_period(self):
        return 2*math.pi*math.sqrt(self.m/self.k)
    def period(self):
        i = 0
        T = 0
        while self.x[i] >= self.x0:
            self.__move(i)
            i += 1
            T += self.dt
        return 2*T 
    def plot_xt(self):
        plt.plot(self.t, self.x)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("Ovisnost pomaka o vremenskom intervalu")
        plt.show()
    def plot_vt(self):
        plt.plot(self.t, self.v)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.title("Ovisnost brzine o vremenskom intervalu")
        plt.show()
    def plot_at(self):
        plt.plot(self.t, self.a)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        plt.title("Ovisnost akceleracije o vremenskom intervalu")
        plt.show()


        
        