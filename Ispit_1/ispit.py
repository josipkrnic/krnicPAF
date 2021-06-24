import math
import matplotlib.pyplot as plt
class Bullet:
    def __init__(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = []
    def __pozivanje_podataka(self,v_0,h_0):
        return print("Kreiran je novi objekt s parametrima v0 = {} m/s i h0 = {} m.".format(v_0,h_0))
    def init(self, h0, v0, dt=0.01):
        self.T = 0
        self.t.append(0)
        self.Y = h0
        self.y.append(self.Y)
        self.X = 0
        self.x.append(self.X)
        self.v_x = v0
        self.v_y = 0
        self.vx.append(self.v_x)
        self.vy.append(self.v_y)
        self.g = -9.81
        self.dt = dt
        self.__pozivanje_podataka(v0,h0)
    def promjena_brzine(self,v):
        self.v_x = v
        print("Nova brzina metka jest {}.".format(self.v_x))
    def promjena_visine(self,h):
        self.Y = h
        print("Nova visina metka jest {}.".format(self.Y))
    def reset(self):
        self.t.clear()
        self.x.clear()
        self.y.clear()
        self.vx.clear()
        self.vy.clear()
    def __move(self,i):
        self.t.append(self.t[i-1] + self.dt)
        self.vx.append(self.vx[i-1] + 0)
        self.vy.append(self.vy[i-1] + self.g*self.dt)
        self.x.append(self.x[i-1] + self.vx[i]*self.dt)
        self.y.append(self.y[i-1] + self.vy[i]*self.dt)
    def tijek_dogadanja(self):
        i = 0
        while self.y[i] > 0:
            self.__move(i)
            i += 1
        return self.x, self.y, self.t, self.vx, self.vy
    def metak_meta(self,h_metak,domet,h_meta,l_meta):
        self.hb = h_metak
        self.D = domet
        self.hm = h_meta
        self.lm = l_meta
        self.vrijeme1 = math.sqrt(2*(self.hb - (self.hm + self.lm))/9.81)
        self.vrijeme2 = math.sqrt(2*(self.hb - (self.hm - self.lm))/9.81)
        self.vrijeme_tocno_u_sridu = math.sqrt(2*(self.hb - self.hm)/9.81)
        self.brzina1 = round(self.D/self.vrijeme1,2)
        self.brzina2 = round(self.D/self.vrijeme2,2)
        self.brzina_tocno_u_sridu = round(self.D/self.vrijeme_tocno_u_sridu,2)
        print("Brzina potrebna za pogoditi metu jest u rasponu od {} m/s do {} m/s.".format(self.brzina1, self.brzina2))
        print("Brzina potrebna za pogoditi točno u sredinu mete jest {} m/s.".format(self.brzina_tocno_u_sridu))
   
        
        
        
    
    
                
            
        
    
        
        
    
        
        
   
        
