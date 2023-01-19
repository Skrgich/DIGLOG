def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]

def registar_zbrajalo_pla():
    x = [int(s) for s in input("Unesite stanja ciklusa: ").replace('->', ' ').replace(',', ' ').split(' ') if s]
    sljed = {}
    for i in range(len(x)):
        sljed[x[i]] = x[(i + 1) % len(x)]

    
    ans = ['' for _ in range(16)]
    for i in range(len(x)):
        dodaj = (sljed[x[i]] - x[i] + 16) % 16
        if dodaj > 4 and dodaj < 12:
            print("Nije moguce rijesiti!")
            return
        ans[i] = (int_to_binary(dodaj, 4)[1:] + '0' if dodaj != 4 else "0111")

    
    ans = [''.join([ans[j][i] for j in range(16)]) for i in range(4)]

    
    print('')
    for i in range(8):
        print("{}: ".format(chr(97 + i)), end = '')
        for j in range(2 ** (i // 2 + 1)):
            print(str(int(i % 2 != j % 2)) * (2 ** (3 - i // 2)), end = '')
        print('')
    
    for j in range(4):
        print("{}: {}".format(chr(97  + 8 + j), ans[j]))
    
    print('\n')


if __name__ == "__main__":
    registar_zbrajalo_pla()