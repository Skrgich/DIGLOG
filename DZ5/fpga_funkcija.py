def fpga_funkcija():
    vars = int(input("Unesite broj ulaza funkcije: "))
    funkcija = input("Unesite funkciju kao produkt maksterma ili suma minterma: ")
    tip = True if funkcija[0] != 'M' else False
    x = list(map(int, funkcija[2:-1].split(',')))
    print('')
    for i in range(2 ** vars):
        print("D{:<2}= {}".format(i, 1 if i in x and tip else 1 if i not in x and not tip else 0))
    print('\n')


if __name__ == "__main__":
    fpga_funkcija()
    
