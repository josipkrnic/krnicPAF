import matplotlib.pyplot as plt
import elektromagnetskopolje as emf
import numpy
p1 = emf.ElektroMagnetskoPolje()
p2 = emf.ElektroMagnetskoPolje()
p1.init(0,0,0,numpy.array((0.1,0.1,0.1)),1,-1,numpy.array((0,0,0)),numpy.array((0,0,1)))
p2.init(0,0,0,numpy.array((0.1,0.1,0.1)),1,-1,numpy.array((0,0,0)),numpy.array((0,0,1)))
x1,y1,z1 = p1.putanja_euler()
x2,y2,z2 = p2.putanja_rungekutta()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1, y1, z1, "red", label="elektron - euler")
ax.plot3D(x2, y2, z2, "b--", label="elektron - runge-kutta")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("z [m]")
ax.set_title("Usporedba gibanja elektrona po euleru i rungekutti")
plt.legend(["euler", "rungekutta"])
plt.show()
p1.reset()
p2.reset()