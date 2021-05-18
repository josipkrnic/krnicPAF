import harmonic_oscilator as harm
import matplotlib.pyplot as plt
import math
p1 = harm.HarmonicOscilator()
p1.init(0, 10)
p1.titranje(10)
p1.plot_xt()
p1.plot_vt()
p1.plot_at()
print("Period titranja iznosi {} s.".format(p1.period()))
p1.reset()
#ovisnost perioda titranja o intervalu dt
period_ = []
Dt = []
analitickiperiod = []
p2 = harm.HarmonicOscilator()
dt0 = 0.001
for i in range(1,100):
    dt0 += 0.001
    Dt.append(dt0)
for dt in Dt:
    p2.init(0, 10, 1, 20, 0, dt)
    p2.titranje(20)
    analitickiperiod.append(p2.analiticki_period())
    period_.append(p2.period())
    p2.reset()
plt.plot(Dt, period_,c="r")
plt.plot(Dt, analitickiperiod, c="b")
plt.xlabel("Dt")
plt.ylabel("Period")
plt.title("Ispravnost perioda titranja u odnosu na veličinu dt")
plt.legend(["Numerički period", "Analitički period"])
plt.show()
rel_error = []
_dt = []
DT0 = 0.001
p3 = harm.HarmonicOscilator()
for i in range(1, 100):
    DT0 += 0.001
    _dt.append(DT0)
for dt in _dt:
    p3.init(0, 10, 1, 20, 0, dt)
    p3.titranje(30)
    T_anal = p3.analiticki_period()
    T_num = p3.period()
    error = abs((T_num - T_anal)/T_anal)*100
    rel_error.append(error)
    p3.reset()
plt.plot(_dt, rel_error)
plt.xlabel("dt [s]")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost relativne pogreške kod računanja\n peroda titranja o intervalu dt")
plt.show()

