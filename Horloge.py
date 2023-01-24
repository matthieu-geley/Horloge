import time

def afficher_heure(hh, mm, ss, ha, ma, sa):
    heure = (hh, mm, ss)
    alarme = (ha, ma, sa)
    heur, min, sec = heure
    heura, mina, seca = alarme
    compte = 1
    while compte > 0:
        if heur == heura and min == mina and sec == seca:
            print("Il est l'heure de se réveiller")
            break
        elif sec == 60:
            sec = 0
            min += 1
            if min == 60:
                min = 0
                heur += 1
        affichage=(f"{heur:02d}"+":"+f"{min:02d}"+":"+f"{sec:02d}")
        print(affichage)
        time.sleep(1)
        sec += 1

def alarme(hh, mm, ss, ha, ma, sa):
    afficher_heure(hh, mm, ss, ha, ma, sa)


alarme(14,42,50,14,42,55)