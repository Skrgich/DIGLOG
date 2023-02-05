from math import floor

def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]

def tablica_kombinacija_napona():
    naponske_raz = sorted(list(map(int, [x[:-1] for x in input("Unesite naponske razine: ").split(' ')])))
    logika = int(input("Unesite 1 za pozitivnu, -1 za negativnu logiku: "))
    if logika == -1: naponske_raz.sort(reverse = True)
    vars = int(input("Unesite broj varijabli: "))
    f = input("Unesite funkciju: ").replace('f=', '').replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    print('')
    for i in range(2 ** vars):
        temp = f
        komb = []
        bin_komb = int_to_binary(i, vars)
        for j in range(vars):
            temp = temp.replace(chr(65 + j), bin_komb[j])

        print("{:2}. redak: ".format(i), end = '')
        for j in bin_komb:
            print("{},".format(naponske_raz[int(j)]), end = '')
        print("{}".format(naponske_raz[int(eval(temp))]))

    print('\n')



if __name__ == "__main__":
    tablica_kombinacija_napona()