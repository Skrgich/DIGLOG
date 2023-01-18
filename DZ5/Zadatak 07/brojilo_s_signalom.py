import logicmin

def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]


def brojilo_u_ciklusu():
    d = {}
    print(' ')

    vars = int(input("Unesite broj bistabila: "))
    bistabil = input("Unesite tip bistabila (D ili T): ").upper()

    x = [int_to_binary(i, 2 + vars) for i in range(2 ** (vars + 2))]
    d0 = int(input("Unesite promjenu trenutnog stanja kada je d = 0: "))
    d1 = int(input("Unesite promjenu trenutnog stanja kada je d = 1: "))



    t = logicmin.TT(2 + vars, vars)
    for i in range(2 ** (vars + 2)):
        komb = x[i]
        izlaz = ''.join('0' for _ in range(vars + 2)) if i >= 2 ** (vars + 1) else x[(i + d1 + 2 ** (vars + 1)) % 2 ** (vars + 1)] if i >= 2 ** (vars) else x[(i + d0 + 2 ** (vars + 1)) % 2 ** (vars + 1)]
        if bistabil == 'D':
            t.add(komb, izlaz)
        elif bistabil == 'T':
            t.add(komb, ''.join('0' if komb[j] == izlaz[j] else '1' for j in range(vars + 2)))

        # print(komb, izlaz, ''.join('0' if komb[j] == izlaz[j] else '1' for j in range(vars + 2)))
    
    sols = t.solve()
    rj = str(sols)
    # print(rj)

    imena_varijabli = ['Q{}'.format(i, bistabil) for i in range(vars)]
    imena_varijabli.extend(['d', 'c'])
    imena_izlaza = ['B{}.{}'.format(i, bistabil) for i in range(vars - 1, -1, -1)]

    rj = rj.split('\n')
    for i in range(len(rj)):
        y, rj[i] = rj[i].split(' <= ')
        rj[i] = rj[i].split(' + ')
        for j in range(len(rj[i])):
            rj[i][j] = rj[i][j].replace('.', ' AND ')
            rj[i][j] = '(' + rj[i][j] + ')'
        if len(rj[i]) == 1: rj[i][j] = rj[i][j][1:-1]
        rj[i] = ' OR '.join(rj[i])
        # print('\n\n{}', rj[i])
        for j in range(len(imena_varijabli)):
            rj[i] = rj[i].replace('x{}\''.format(j), 'NOT x{}'.format(j))
        for j in range(len(imena_varijabli)):
            rj[i] = rj[i].replace('x{}'.format(j), imena_varijabli[j])
        rj[i] = imena_izlaza[len(rj) - 1 - i] + ' <= ' + rj[i]

    print('')
    for rjesenje in rj[::-1]:
        print(rjesenje)
    print('\n')

if __name__ == "__main__":
    brojilo_u_ciklusu()