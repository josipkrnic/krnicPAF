import math
import numpy 
import matplotlib.pyplot as plt
class ElektroMagnetskoPolje:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
    def init(self, x0, y0, z0, v0, m, Q, elekpolje, magnpolje, dt=0.01):
        self.v = v0
        self.m = m
        self.x.append(x0)
        self.y.append(y0)
        self.z.append(z0)
        self.q = Q
        self.E = elekpolje
        self.B = magnpolje
        self.a = numpy.array((0,0,0))
        self.dt = dt
    def reset(self):
        self.x.clear()
        self.y.clear()
        self.z.clear()
    def __move_euler(self, i):
        self.a = (self.q)*(self.E + numpy.cross(self.v,self.B)/self.m)
        self.v = self.v + self.a*self.dt
        self.x.append(self.x[i-1] + self.v[0]*self.dt)
        self.y.append(self.y[i-1] + self.v[1]*self.dt)
        self.z.append(self.z[i-1] + self.v[2]*self.dt)
    def __move_rungekutta(self, i):
        k1v = (self.q/self.m)*(self.E + numpy.cross(self.v,self.B))*self.dt
        k1r = self.v * self.dt
        k2v = (self.q/self.m)*(self.E + numpy.cross(self.v+k1v/2,self.B))*self.dt
        k2r = (self.v + k1v/2) * self.dt
        k3v = (self.q/self.m)*(self.E + numpy.cross(self.v+k2v/2,self.B))*self.dt
        k3r = (self.v + k2v/2) * self.dt
        k4v = (self.q/self.m)*(self.E + numpy.cross(self.v+k3v/2,self.B))*self.dt
        k4r = (self.v + k3v/2) * self.dt
        self.v = self.v + (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[i-1] + (k1r[0] + 2*k2r[0] + 2*k3r[0] + k4r[0])/6)
        self.y.append(self.y[i-1] + (k1r[1] + 2*k2r[1] + 2*k3r[1] + k4r[1])/6)
        self.z.append(self.z[i-1] + (k1r[2] + 2*k2r[2] + 2*k3r[2] + k4r[2])/6)
    def putanja_euler(self, T=30):
        DT = int(T/0.01)
        i = 0
        while i < DT:
            self.__move_euler(i)
            i += 1
        return self.x, self.y, self.z
    def putanja_rungekutta(self, T=30):
        DT = int(T/0.01)
        i = 0
        while i < DT:
            self.__move_euler(i)
            i += 1
        return self.x, self.y, self.z
