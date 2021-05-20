import math
import matplotlib.pyplot as plt
class Projectile:
    g = -9.81 #akceleracija slobodnog pada, u metrima po kvadratnoj sekundi
    def __init__(self):
        self.t = []
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []
    def init(self, v0, x0, y0, theta0, ro_zrak=1.22, Cd=1, masa=1, povrsina=0.001, dt=0.01): #m je masa tijela u kilogramima, a A površina tijela u metrima kvadratnim
        self.t.append(0)
        self.m = masa
        self.A = povrsina
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
    def __move(self, i):
        self.t.append(self.t[i-1]+self.dt)
        self.vx.append(self.vx[i-1] + (-1)*self.vx[i]*self.vx[i]*self.o*self.dt)
        self.vy.append(self.vy[i-1] + self.g*self.dt + self.vy[i]*self.vy[i]*self.o*self.dt)
        self.x.append(self.x[i-1]+self.vx[i]*self.dt)
        self.y.append(self.y[i-1]+self.vy[i]*self.dt)
    def otpor_zraka_x(self, x, v, t):
        return -1*((self.ro*self.CD*self.A)/(2*self.m))*v**2
    def otpor_zraka_y(self, x, v, t):
        return -1*((self.ro*self.CD*self.A)/(2*self.m))*abs(v)*v
    def __move_Runge_Kutta(self, i):
        self.t.append(self.t[i-1] + self.dt)
        k1vx = (self.otpor_zraka_x(self.x[i-1], self.vx[i-1], self.t[i-1]))*self.dt
        k1vy = (self.g + self.otpor_zraka_y(self.y[i-1], self.vy[i-1], self.t[i-1]))*self.dt
        k1x = self.vx[i-1]*self.dt
        k1y = self.vy[i-1]*self.dt
        k2vx = (self.otpor_zraka_x(self.x[i-1]+k1x/2, self.vx[i-1]+k1vx/2, self.t[i-1]+self.dt/2))*self.dt
        k2vy = (self.g + self.otpor_zraka_y(self.y[i-1]+k1y/2, self.vy[i-1]+k1vy/2, self.t[i-1]+self.dt/2))*self.dt
        k2x = (self.vx[i-1]+k1vx/2)*self.dt
        k2y = (self.vy[i-1]+k1vy/2)*self.dt
        k3vx = (self.otpor_zraka_x(self.x[i-1]+k2x/2, self.vx[i-1]+k2vx/2, self.t[i-1]+self.dt/2))*self.dt
        k3vy = (self.g + self.otpor_zraka_y(self.y[i-1]+k2y/2, self.vy[i-1]+k2vy/2, self.t[i-1]+self.dt/2))*self.dt
        k3x = (self.vx[i-1]+k2vx/2)*self.dt
        k3y = (self.vy[i-1]+k2vy/2)*self.dt
        k4vx = (self.otpor_zraka_x(self.x[i-1]+k3x/2, self.vx[i-1]+k3vx/2, self.t[i-1]+self.dt/2))*self.dt
        k4vy = (self.g + self.otpor_zraka_y(self.y[i-1]+k3y/2, self.vy[i-1]+k3vy/2, self.t[i-1]+self.dt/2))*self.dt
        k4x = (self.vx[i-1]+k3vx/2)*self.dt
        k4y = (self.vy[i-1]+k3vy/2)*self.dt
        self.vx.append(self.vx[i-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.vy.append(self.vy[i-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.x.append(self.x[i-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y.append(self.y[i-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
    def range(self):
        i = 0
        while self.y[i] >= 0:
            self.__move(i)
            i += 1
        return self.x, self.y
    def rangeRungeKutta(self):
        i = 0
        while self.y[i] >= 0:
            self.__move_Runge_Kutta(i)
            i += 1
        return self.x, self.y
    
        
