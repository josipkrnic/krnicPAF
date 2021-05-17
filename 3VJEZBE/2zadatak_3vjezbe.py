import Particle as prt
import matplotlib.pyplot as plt
import math
relativna_greska = []
Dt = []
dt0 = 0.001
p1 = prt.Particle()
p1.init(10, 0, 0, 60, 0.01)
D = (10**2)*math.sin(math.radians(120))/9.81
print("Analitički domet jest {} m, a numerički {} m.".format(round(D,3), round(p1.range(),3)))
p1.range()
p2 = prt.Particle()
for i in range(0,100):
    dt0 = dt0 + 0.001
    Dt.append(dt0)
for dt in Dt:
    p2.init(10, 0, 0, 60, dt)
    rel_greska = (abs(p2.range()-D)/D)*100
    relativna_greska.append(rel_greska)
    p2.reset()
plt.plot(Dt, relativna_greska)
plt.xlabel("vremenski interval(dt) [s]")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost relativne pogreške računanja\n u odnosu na veličinu dt intervala: ")
plt.show()





 
