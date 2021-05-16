import Projectile as prj
import matplotlib.pyplot as plt
p1 = prj.Projectile()
p1.init(30, 0, 0, 45, 1.22, 1, 1, 0.001, 0.01)
print("Za v0 = {} i kut = {}, domet kosog hica jest {} metara.".format(50,45,round(p1.range(),3)))
p1.range()
p1.plot()
p1.reset()
