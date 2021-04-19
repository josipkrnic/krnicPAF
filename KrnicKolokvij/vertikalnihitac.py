import math
class VertikalniHitac():
    g = -9.81
    def __init__(self):
        self.t = []
        self.v = []
        self.h = []
        self.a = []
        self.h_otpor = []
        self.v_otpor = []
        self.t_otpor = []
        self.a_otpor = []
        self.k = []
        self.m = []
    def init(self,h0,v0,dt=0.01):
        self.t.append(0)
        self.h.append(h0)
        self.v.append(v0)
        self.a.append(self.g)
        self.dt = dt
        print("Objekt je uspješno stvoren s početnom brzinom {} m/s i početnom visinom {} m.".format(v0,h0))
    def init_otpor(self,H0,V0,konst, Dt=0.01,masa=1):
        self.t_otpor.append(0)
        self.h_otpor.append(H0)
        self.v_otpor.append(V0)
        self.a_otpor.append(self.g)
        self.Dt = Dt
        self.k.append(konst)
        self.m.append(masa)
        print("Objekt je uspješno stvoren s početnom brzinom {} i početnom visinom {}.".format(V0,H0))
    def reset(self):
        self.t.clear()
        self.h.clear()
        self.v.clear()
        self.a.clear()
    def reset_otpor(self):
        self.t_otpor.clear()
        self.h_otpor.clear()
        self.v_otpor.clear()
        self.a_otpor.clear()
    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a.append(self.g)
        self.v.append(self.v[i-1] + self.a[i]*self.dt)
        self.h.append(self.h[i-1] + self.v[i]*self.dt)
    def __move_otpor(self, i):
        self.t_otpor.append(self.t_otpor[i-1] + self.Dt)
        self.a_otpor.append(self.g + (self.k[i]*self.v_otpor[i])/self.m)
        self.v_otpor.append(self.v_otpor[i-1] + self.a_otpor[i]*self.Dt)
        self.h_otpor.append(self.h_otpor[i-1] + self.v_otpor[i]*self.Dt)
    def vrijeme_hica(self):
        i = 0
        while self.h[i] >= 0:
            self.__move(i)
            i += 1
        return self.t[i]
    def h_maks(self):
        i = 0
        while self.v[i] >= 0:
            self.__move(i)
            i += 1
        return self.h[i]
    def vrijeme_hica_otpor(self, m, k):
        i = 0
        while self.h_otpor[i] >= 0:
            self.__move(i)
            i += 1
        return self.t_otpor[i]
            






    
    
        



