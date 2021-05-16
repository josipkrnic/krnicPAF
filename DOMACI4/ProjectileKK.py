import math
import matplotlib.pyplot as plt
class ProjectileKK:
    g = -9.81 #akceleracija slobodnog pada, u metrima po kvadratnoj sekundi
    def __init__(self):
        self.t = []
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []
    def init(self, v0, x0, y0, theta0, ro_zrak=1.22, Cd=1, masa=1, radijus = 0.1, dt=0.01): 
        self.t.append(0)
        self.m = masa
        self.r = radijus
        self.A = 4*3.1415926*self.r*self.r
        self.CD = Cd
        self.ro = ro_zrak
        self.o = (self.ro*self.CD*self.A)/(2*self.m)
        self.vx.append(v0*math.cos(math.radians(theta0)))
        self.vy.append(v0*math.sin(math.radians(theta0)))
        self.x.append(x0)
        self.y.append(y0)
        self.dt = dt
    def reset(self):
        self.t.clear()
        self.x.clear()
        self.y.clear()
        self.vx.clear()
        self.vy.clear()
    def promjena_objekta(self, a, theta):
        self.A = a*a*(math.sin(math.radians(theta)) + math.cos(math.radians(theta)))
        return print("Podaci su modificirani za kosi hitac kocke duljine stranice {} pod početnim kutem theta.".format(a))
    def __move(self, i):
        self.t.append(self.t[i-1]+self.dt)
        self.vx.append(self.vx[i-1] + (-1)*self.vx[i]*self.vx[i]*self.o*self.dt)
        self.vy.append(self.vy[i-1] + self.g*self.dt + self.vy[i]*self.vy[i]*self.o*self.dt)
        self.x.append(self.x[i-1]+self.vx[i]*self.dt)
        self.y.append(self.y[i-1]+self.vy[i]*self.dt)
    def range(self):
        i = 0
        while self.y[i] >= 0:
            self.__move(i)
            i += 1
        return self.x[i]
    def plot(self):
        plt.plot(self.x,self.y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("x,y")
        plt.show()
        

