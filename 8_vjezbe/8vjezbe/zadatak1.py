import Projectile as prj
import matplotlib.pyplot as plt
p1 = prj.Projectile()
p1.init(30, 0, 0, 45, 1.22, 1, 1, 0.001, 0.01)
x,y = p1.range()
print("Domet kosog hica po Eulerovoj metodi za zadane početne uvjete jest {} m.".format(round(max(x),3)))
plt.plot(x,y,c="r")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()
p1.reset()
