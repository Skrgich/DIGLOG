

from fpga_funkcija import fpga_funkcija
from clb_fpga import CLB_FPGA
from lut_d_bistabil import lut_d_bistabil
from posmacni_reg import main
from brojilo_u_ciklusu import brojilo_u_ciklusu
from brojilo_s_signalom import brojilo_s_signalom
from brojilo_u_standardno import brojilo_u_standardno
from brojilo_s_memorijom import brojilo_s_memorijom
from registar_zbrajalo_pla import registar_zbrajalo_pla
from lut_sekvenca import LUT_sekvenca
from vrijeme_pretvorbe import vrijeme_pretvorbe



if __name__ == "__main__":
    while True:
        print('\nUnesite broj zadatka koji zelite rijesiti:\n0 za izlaz, -1 za help')
        x = int(input())
        print('\n')
        if x == 0: break
        elif x == 1: fpga_funkcija()
        elif x == 2: CLB_FPGA()
        elif x == 3: lut_d_bistabil()
        elif x == 4: main()
        elif x == 6: brojilo_u_ciklusu()
        elif x == 7: brojilo_s_signalom()
        elif x == 9: brojilo_u_standardno()
        elif x == 10: brojilo_s_memorijom()
        elif x == 11: registar_zbrajalo_pla()
        elif x == 12: LUT_sekvenca()
        elif x == 13: vrijeme_pretvorbe()
        elif x == -1:
            d = {
                1: "Konfigurabilni logički blok (CLB) sklopa FPGA ostvaren je uporabom pregledne tablice (LUT) s n ulaza, kako je prikazano slikom. Uporabom takvog CLB-a potrebno je realizirati funkciju f zadanu kao suma/produkt minterma/maxterma...",
                2: "Konfigurabilni logički blok (CLB) sklopa FPGA ostvaren je uporabom pregledne tablice (LUT) s n ulaza, kako je prikazano slikom. Uporabom takvog CLB-a potrebno je realizirati funkciju: f(A,B,...",
                3: "Na raspolaganju je n-ulazni LUT s D bistabilom, prikazan slikom...",
                4: "Potrebno je projektirati sklop koji će prolaziti kroz sljedeća stanja: (...). Sklop je potrebno ostvariti uporabom strukture prikazane na slici (posmačni registar + dekoder/mux)...",
                6: "Potrebno je realizirati sinkrono brojilo koje broji u ciklusu: (...), ako je na raspolaganju n D/T/SR/JK bistabila...",
                7: "Uporabom D/T/SR/JK bistabila realizirati n-bitno brojilo koji broji ovisno o signalu d: ako je d=1, tad je sljedeće_stanje = trenutno_stanje +- n, inače sljedeće_stanje = trenutno_stanje +- n",
                9: "Brojilo B koje je iskorišteno za brojanje broji u ciklusu (...) Programirajte memoriju tako da se čitav sklop ponaša kao standardno binarno brojilo unaprijed...",
                10: "Memorije R1 i R2 potrebno je programirati tako da se dobije brojilo koje broji u ciklusu...",
                11: "Uporabom registra, binarnog zbrajala i sklopa PLA želi se ostvariti brojilo koje broji u ciklusu...",
                12: "Logički blok FPGA sklopa temeljen na LUT-u, bistabilu i multipleksoru prikazan je na sljedećoj slici... Programirajte sve logičke blokove tako da se dobije sklop koji na izlazu generira sekvencu:...",
                13: "Za neki n-bitni pretvornik sa sukcesivnom aproksimacijom poznato je da se ulazni napon iznosa..."
            } 
            print("\nUkoliko je redoslijed razlicit, u nastavku je tekst svakog zadatka:\n")
            for k in d:
                print('{}:\t{}\n'.format(k, d[k]))

        print('\n\n')
        