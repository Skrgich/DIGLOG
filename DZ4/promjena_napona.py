def promjena_napona():

    napon = float(input("Unesite napon: ").replace('V', ''))
    frekvencija = float(input("Unesite frekvenciju: ").lower().replace('mhz', ''))

    p = int(input("Unesite promjenu frekvencije: ").replace('%', ''))

    novi_napon = napon / ( (1.0 + p / 100)) ** 0.5
    
    if novi_napon > napon: print("Napon treba povecati na {:.5}".format(novi_napon))
    else: print("Napon treba smanjiti na {:.5}V".format(novi_napon))




if __name__ == "__main__":
    promjena_napona()