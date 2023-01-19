

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
        elif x == 1: CLB_FPGA()
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
            print("Nedostupno")
        print('\n\n')
        