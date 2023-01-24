import time

def afficher_heure(hh, mm, ss, ha, ma, sa):
    heure = (hh, mm, ss)
    heur, min, sec = heure
    compte = 1
    while compte > 0:
        sec += 1
        if heur == ha and min == ma and sec == sa:
            print("Il est l'heure de se réveiller")
            break
        if sec == 60:
            sec = 00
            min += 1
        if min == 60:
            min = 00
            heur += 1
        affichage=(f"{heur:02d}"+":"+f"{min:02d}"+":"+f"{sec:02d}")
        print(affichage)
        time.sleep(1)

def alarme(hh, mm, ss, ha, ma, sa):
    afficher_heure(hh, mm, ss, ha, ma, sa)


alarme(14,42,50,14,43,59)