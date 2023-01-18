def lut_d_bistabil():
    d = {
        0 : {'NQ' : '1', 'Q' : '0', '1': '1', '0': '0'},
        1 : {'NQ' : '0', 'Q' : '1', '1': '1', '0': '0'}
    }
    vars = int(input("Unesite broj ulaza funkcije: "))
    st = input("Unesite stanja za Qn+1 (\'0\', \'1\', \'Q\' i \'NQ\'): ").split(' ')

    print('')
    for i in range(2 ** (vars)):
        ind = i % 2 ** (vars - 1)
        print("LUT_{:<2} = {}".format( i, d[i // 2 ** (vars - 1) ][st[ind]]))
    print('\n')
    
if __name__ == "__main__":
    lut_d_bistabil()