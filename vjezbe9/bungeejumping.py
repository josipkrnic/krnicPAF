import matplotlib.pyplot as plt
class BungeeJumping: 
    def __init__(self, Y0, L0, masa, konstanta, ro_zrak = 1.225, Cd = 1, povrsina = 0.1, otpor = False):
        self.y = []
        self.t = []
        self.Ek = []
        self.Egp = []
        self.Eep = []
        self.E = []
        self.y0 = Y0
        self.l0 = L0
        self.k = konstanta
        self.m = masa
        self.ro = ro_zrak
        self.CD = Cd
        self.A = povrsina
        self.o = otpor
        self.y_ = Y0
        self.v = 0 
        self.t_ = 0 
        self.y.append(self.y0)
        self.t.append(self.t_)
        self.Egp_ = self.m * 9.81 * self.y_
        self.Ek_ = 0 
        self.Eep_ = 0
        self.E_ = self.Ek_ + self.Egp_ + self.Eep_
        self.Ek.append(self.Ek_)
        self.Egp.append(self.Egp_)
        self.Eep.append(self.Eep_)
        self.E.append(self.E_)
    def reset(self):
        self.y.clear()
        self.t.clear()
        self.Ek.clear()
        self.Egp.clear()
        self.Eep.clear()
        self.E.clear()
    def elasticna_sila(self):
        d = self.y0 - self.y_ - self.l0
        if d > 0:
            Fel = self.k*d
        else:
            Fel = 0
        return Fel
    def elasticna_potencijalna_energija(self):
        d = self.y0 - self.y_ - self.l0
        if d > 0:
            Eel = 0.5*self.k*d*d
        else:
            Eel = 0
        return Eel
    def otpor_zraka(self):
        O_Z = - abs(self.v)*self.v*self.ro*self.CD*self.A*0.5
        return O_Z
    def __move(self, dt):
        a = -9.81 + self.elasticna_sila()/self.m
        self.v += a*dt
        self.y_ += self.v*dt
        self.t_ += dt
        self.Egp_ = self.m*9.81*self.y_
        self.Ek_ = 0.5*self.m*self.v*self.v
        self.Ee_ = self.elasticna_potencijalna_energija()
        self.E_ = self.Egp_ + self.Ek_ + self.Eep_
        self.y.append(self.y_)
        self.t.append(self.t_)
        self.Egp.append(self.Egp_)
        self.Ek.append(self.Ek_)
        self.Eep.append(self.Eep_)
        self.E.append(self.E_)
    def __move_otpor(self, dt):
        a = -9.81 + (self.elasticna_sila() + self.otpor_zraka())/self.m
        self.v += a*dt
        self.y_ += self.v*dt
        self.t_ += dt
        self.Egp_ = self.m*9.81*self.y_
        self.Ek_ = 0.5*self.m*self.v*self.v
        self.Eep_ = self.elasticna_potencijalna_energija()
        self.E_ = self.Ek_ + self.Egp_ + self.Eep_
        self.y.append(self.y_)
        self.t.append(self.t_)
        self.Egp.append(self.Egp_)
        self.Ek.append(self.Ek_)
        self.Eep.append(self.Eep_)
        self.E.append(self.E_)
    def move(self ,T ,dt):
        if self.o:
            while self.t_ < T:
                self.__move_otpor(dt)
        else:
            while self.t_ < T:
                self.__move(dt)


