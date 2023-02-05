

from automat import automat
from xor_rotacija import xor_rotacija
from RAM_funkcija import RAM_funkcija
from p1_p2_pobuda import p1_p2_pobuda
from promjena_napona import promjena_napona
from tablica_kombinacija_napona import tablica_kombinacija_napona

if __name__ == "__main__":
    while True:
        print('\nUnesite broj zadatka koji zelite rijesiti:\n0 za izlaz, -1 za help')
        x = int(input())
        print('\n')
        if x == 0: break
        elif x == 1: p1_p2_pobuda()
        elif x == 2: tablica_kombinacija_napona()
        elif x == 3: promjena_napona()
        elif x == 7: RAM_funkcija()
        elif x == 8: xor_rotacija()
        elif x == 9: automat()
        elif x == -1:
            d = {
                1: "Na raspolaganju su sklopovi podskupine P1 i P2 čiji su parametri zadani kako slijedi...",
                2: "Neki digitalni sklop prikazan slikom koristi naponsku logiku, te logička stanja prikazuje naponskim razinama...",
                3: "Digitalni sustav radi s naponom napajanja od 7V i na frekvenciji od 127MHz. Uz pretpostavku da se napon napajanja moze mijenjati (uz ispravan rad sustava), kako treba promijeniti napon ako se zeli...",
                7: "Zadana je uređena n-torka P=(...). Funkcija F(i) vraća i-ti element od P (npr. F(n) = m). Projektirati sklop koji ostvaruje ovu funkciju...",
                8: "Funkcija f(n) svakom n iz skupa {0,…,15} pridružuje broj (n XOR m), gdje je m jednak broju n zarotiranom...",
                9: "Stroj s konačnim brojem stanja zadan je tablicom u nastavku. Stroj ima jedan jednobitni ulaz, te jedan n-bitni izlaz... Za realizaciju tog stroja na raspolaganju je n bistabila..."
            } 
            print("\nUkoliko je redoslijed razlicit, u nastavku je tekst svakog zadatka:\n")
            for k in d:
                print('{}:\t{}\n'.format(k, d[k]))

        print('\n\n')
        