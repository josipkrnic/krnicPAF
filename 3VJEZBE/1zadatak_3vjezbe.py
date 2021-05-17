import Particle as prt
import matplotlib.pyplot as plt
import math
p1 = prt.Particle()
p1.init(10, 0, 0, 60, 0.001)
D = (10**2)*math.sin(math.radians(120))/(9.81)
print("Domet kosog hica izračun analitički jest {} metara, a numerički {} metara.".format(round(D, 3), round(p1.range(),3)))
p1.range()
p1.plot_trajectory()
p1.reset()
