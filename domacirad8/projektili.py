import math
import matplotlib.pyplot as plt
class Projektili:
    def __init__(self):
        self.t = []
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []
    def init(self, v0, theta, x0, y0, povrsina, radijus = 0.01, brid = 0.02, masa = 10, ro_zrak = 1.22, Cd = 1, dt = 0.01):
        self.t.append(0)
        self.vx.append(v0*math.cos(math.radians(theta)))
        self.vy.append(v0*math.sin(math.radians(theta)))
        self.x.append(x0)
        self.y.append(y0)
        self.m = masa
        self.CD = Cd
        self.ro = ro_zrak
        self.povrsina = povrsina
        self.r = radijus
        self.a = brid
        self.dt = dt
        if povrsina == 1: #inicijalniziranjem varijable povrsina pod brojem 1 računamo domet za kuglu
            self.A = (self.r**2)*4*3.1415
        elif povrsina == 2:#inicijaliziranjem varijable povrsina pod brojem 2 računamo domet za kocku
            self.A = (self.a**2)*(math.sin(math.radians(theta))+ math.cos(math.radians(theta)))
        else: #inicijalizacijom varijable povrsina pod bilo kojim drugim brojem računamo domet za tijelo nebitnog oblika
            self.A = 0.001 
        self.otpor = (self.A*self.ro*self.CD*self.dt)/(2*self.m)
    def reset(self):
        self.t.clear()
        self.vx.clear()
        self.vy.clear()
        self.x.clear()
        self.y.clear()
    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.vx.append(self.vx[i-1] + (-1)*(self.vx[i]**2)*self.otpor)
        self.vy.append(self.vy[i-1] + (-9.81)*self.dt + (-1)*abs(self.vy[i])*self.vy[i]*self.otpor)
        self.x.append(self.x[i-1] + self.vx[i]*self.dt)
        self.y.append(self.y[i-1] + self.vy[i]*self.dt)
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
        plt.title("x,y graf")
        plt.show()