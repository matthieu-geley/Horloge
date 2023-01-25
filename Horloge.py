import time
from time import strftime


def alarme(heure, minute, seconde):
    heura = 13
    minuta = 15
    seconda = 50
    if heure == heura and minute == minuta and seconde == seconda:
        print("Il est l'heure de se réveiller")
        return False

def afficher_heure():
    heure = int(strftime('%H'))
    minute = int(strftime('%M'))
    seconde = int(strftime('%S'))
    i = 0
    while i == 0:
        if seconde == 60:
            seconde = 0
            minute += 1
            if minute == 60:
                minute = 0
                heure += 1
        affichage=(str(heure).rjust(2,'0')+":"+str(minute).rjust(2,'0')+":"+str(seconde).rjust(2,'0'))
        seconde += 1
        print(affichage)
        if alarme(heure, minute, seconde) == False:
            i = 1
        time.sleep(1)

afficher_heure()
