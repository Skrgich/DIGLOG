def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]

def LUT_sekvenca():
    x = [int(s) for s in input("Unesite sekvencu: ").replace('->', ' ').replace(',', ' ').split(' ') if s]

    luts = [int_to_binary(s, 4) for s in x]

    out = ['0,1,1,0', '1,0,1,0']
    for i in range(4):
        out.append(','.join([luts[j][i] for j in range(4)]))
    
    print('')
    for i in range(6):
        print("L{}.lut: {}".format(i + 1, out[i]))
        print("L{}.s  : {}".format(i + 1, 1 if i < 2 else 0))
    print('\n')



if __name__ == "__main__":
    LUT_sekvenca()