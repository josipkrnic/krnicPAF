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
    for i in range(1,100): #za 100 različitih objekta gdje će se koeficijent trenja kretati od 1 do 11 u koracima po 0.05, a masa od 1 do 51 u koracima od 0.5
        C_d += 0.05
        m_0 += 0.5
        Koef_tr.append(C_d)
        masa.append(m_0)
    for Cd in Koef_tr:
        p1.init(50, 0, 0, 45, 1.22, Cd, 1, 0.001, 0.01) 
        x,y = p1.range()
        Domet.append(max(x))
        p1.reset()
    for m in masa:
        p2.init(50, 0, 0, 45, 1.22, 1, m, 0.001, 0.01)
        X,Y = p2.range()
        domet.append(max(X))
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

