import universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sunce", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
merkur = universe.Planet("Merkur", 3.3022e23, np.array((0.,0.387*au)),np.array((-47861,0.)))
venera = universe.Planet("Venera", 4.869e24, np.array((-0.722*au,0.)),np.array((0., -34965)))
earth = universe.Planet("Zemlja", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))
mars = universe.Planet("Mars", 6.4185e23, np.array((0.,-1.52*au)), np.array((23885, 0.)))
komet = universe.Planet("Komet", 5*10**15, np.array((2.8*au, 2.8*au)), np.array((-25000., -18000.)))
ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(merkur)
ss.add_planet(venera)
ss.add_planet(earth)
ss.add_planet(mars)
ss.add_planet(komet)

ss.evolve(2*year)

fig= plt.figure(figsize=(10,10))
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(sun.x,sun.y,label=sun.name,color="yellow", linewidth=5.0)
plt.plot(merkur.x, merkur.y, label=merkur.name, color="green")
plt.plot(venera.x, venera.y, label=venera.name, color="gold")
plt.plot(earth.x,earth.y,label=earth.name,color="blue")
plt.plot(mars.x,mars.y,label=mars.name,color="red")
plt.plot(komet.x,komet.y,label=komet.name,color="brown")

plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y graf')
plt.legend(loc="upper right")
plt.savefig("komet_u_suncevu_sustavu.pdf")
plt.show()
