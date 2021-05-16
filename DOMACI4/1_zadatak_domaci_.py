import ProjectileKK as pkk
import matplotlib.pyplot as plt
p1 = pkk.ProjectileKK()
p1.init(50, 0, 0, 45, 1.22, 1, 1, 0.1, 0.01)
print("Domet kosog hica kugle jest {} metara".format(round(p1.range(),3)))
p1.range()
p1.plot()
p1.reset()
p2 = pkk.ProjectileKK()
p2.init(50, 0, 0, 45, 1.22, 1, 1, 0.1, 0.01)
p2.promjena_objekta(0.1, 45)
print("Domet kosog hica kocke jest {} metara.".format(round(p2.range(),3)))
p2.range()
p2.plot()
p2.reset()

