import numpy 
import elektromagnetskopolje as emf
import matplotlib.pyplot as plt
p1 = emf.ElektroMagnetskoPolje() #elektron
p2 = emf.ElektroMagnetskoPolje() #pozitron
p1.init(0,0,0,numpy.array((0.1,0.1,0.1)),1,-1,numpy.array((0,0,0)),numpy.array((0,0,1)))
p2.init(0,0,0,numpy.array((0.1,0.1,0.1)),1,1,numpy.array((0,0,0)),numpy.array((0,0,1)))
x1, y1, z1 = p1.putanja_euler(20)
x2, y2, z2 = p2.putanja_euler(20)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, c="r", label="elektron")
ax.plot3D(x2, y2, z2, c="b", label="pozitron")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("z [m]")
ax.set_title("Usporedba gibanja elektrona i pozitrona u jednolikom magnetskom polju")
plt.legend(["elektron", "pozitron"])
plt.show()
p1.reset()
p2.reset()



