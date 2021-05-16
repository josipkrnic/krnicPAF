import Projectile as prj
import matplotlib.pyplot as plt
def domet_o_trenju():
    Domet = []
    domet = []
    Koef_tr = []
    masa = []
    p1 = prj.Projectile()
    p2 = prj.Projectile()
    C_d = 1
    m_0 = 1
    for i in range(1,500):#za petsto različitih objekata
        C_d += 0.01#svaki sljedeći CD će biti za 0.01 veći od prethodnog
        m_0 += 0.1 #svaka sljedeća masa bit će za 0.1 kg veća od prethodne
        Koef_tr.append(C_d)
        masa.append(m_0)
    for Cd in Koef_tr:
        p1.init(50, 0, 0, 45, 1.22, Cd, 1, 0.001, 0.01) 
        D = p1.range()
        Domet.append(D)
        p1.reset()
    for m in masa:
        p2.init(50, 0, 0, 45, 1.22, 1, m, 0.001, 0.01)
        d = p2.range()
        domet.append(d)
        p2.reset()
    plt.plot(Koef_tr, Domet)
    plt.title("Promjena dometa u odnosu na koeficijent trenja zraka")
    plt.xlabel("Koeficijent trenja zraka")
    plt.ylabel("Domet u metrima [m]")
    plt.show()
    plt.plot(masa, domet)
    plt.title("Promjena dometa u odnosu na masu ispaljenog objekta")
    plt.xlabel("Masa u kilogramima [kg]")
    plt.ylabel("Domet u metrima [m]")
    plt.show()
domet_o_trenju()
