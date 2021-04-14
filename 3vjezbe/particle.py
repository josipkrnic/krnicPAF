import numpy as np
import matplotlib.pyplot as plt
class Particle:
    g = -9.81
    def __init__(self):
        self.x = []
        self.y = []
        self.t = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
    def init(self, v, theta, x0, y0, dt=0.001):
        theta2 = theta*math.pi/180
        self.x.append(x0)
        self.y.append(y0)
        self.t.append(0)
        self.vx.append(v*math.cos(theta2))
        self.vy.append(v*math.sin(theta2))
        self.ax(0)
        self.ay(g)
        self.dt = dt
    def reset(self):
        self.x.clear()
        self.y.clear()
        self.t.clear()
        self.vx.clear()
        self.vy.clear()
        self.ax.clear()
        self.ay.clear()
    def __move(self, i):
        self.x.append(self[x-i] + self.vx[i]*self.dt)
        self.y.append(self[y-i] + self.vy[i]*self.dt)
        self.t.append(self[i-1] + self.dt)
        self.vx.append(self.vy[i-1] + self.ax[i]*self.dt)
        self.vy.append(self.vy[i-1] + self.ay[i]*self.dt)
        self.ax.append(0)
        self.ay.append(self.g)
    def range(self):
        i = 0
        while self.y[i] >= 0:
            self.__move(i)
            i += 1
        return self.x[i]
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('x-y graf')

        v= math.sqrt(self.v_x[0]**2 + self.v_y[0]**2)
        fig.savefig(self.name + ".pdf")