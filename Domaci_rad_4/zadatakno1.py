import matplotlib.pyplot as plt
import projektili as pktl
p1 = pktl.Projektili()
p1.init(50, 45, 0, 0, 1) #broj 1 označava da se radi o kugli
print("Domet kosog hica kugle jest {} metara.".format(round(p1.range(),3)))
p1.range()
p1.plot()
p1.reset()
p2 = pktl.Projektili()
p2.init(50, 45, 0, 0, 2) #broj 2 označava da se radi o kocki
print("Domet kosog hica kocke brida a jest {} metara.". format(round(p2.range(), 3)))
p2.range()
p2.plot()
p2.reset()
p3 = pktl.Projektili()
p3.init(50, 45, 0, 0, 3) #broj 3 (ili bilo koji drugi) označava da se radi o nasumično izabranom tijelu
print("Domet kosog hica nasumičnog tijela standardizirane površine A = 0.001 iznosi {} metara.".format(round(p3.range(), 3)))
p3.range()
p3.plot()
p3.reset()
def razlika_dometa():
    domet_kocke = []
    domet_kugle = []
    radius = []
    brid = []
    p4 = pktl.Projektili()
    p5 = pktl.Projektili()
    r_0 = 0.01 #metara
    a_0 = 0.01 #metara, da promjer kugle bude ekvivalentan bridu kocke
    for i in range(1,100):
        r_0 += 0.01 #metara
        a_0 += 0.01 #metara
        radius.append(r_0)
        brid.append(a_0)
    for radijus in radius:
        p4.init(50, 45, 0, 0, 1, radijus, 0.01, 10, 1.22, 1, 0.01)
        D_kugla = p4.range()
        domet_kugle.append(D_kugla)
        p4.reset()
    for stranica in brid:
        p5.init(50, 45, 0, 0, 2, 0.01, stranica, 10, 1.22, 1, 0.01)
        D_kocka = p5.range()
        domet_kocke.append(D_kocka)
        p5.reset()
    plt.plot(radius, domet_kugle, "b")
    plt.plot(brid, domet_kocke, "r")
    plt.legend(["Domet o radijusu", "Domet o bridu"])
    plt.xlabel("Duljina brida kocke")
    plt.ylabel("Domet kocke")
    plt.title("Ovisnost dometa kugle/kocke o promjeni duljine njihova\n radijusa/brida uz jednake početne parametre")
    plt.show()
razlika_dometa()
