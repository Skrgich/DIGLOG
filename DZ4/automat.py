import logicmin

def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000000' + binary_string)[-size:]

def bist_pobuda(bis, poc, sljed):
    d = {
        'D': {"00" : "0",
              "01" : "1",
              "10" : "0",
              "11" : "1"},
        'T': {"00" : "0",
              "01" : "1",
              "10" : "1",
              "11" : "0"},
        'SR' : {"00" : "0X",
               "01" : "10",
               "10" : "01",
               "11" : "X0"},
        'JK' : {"00" : "0X",
                "01" : "1X",
                "10" : "X1",
                "11" : "X0"}
    }
    return d[bis][poc + sljed]

def automat():
    vars = int(input("Unesite broj bitova: "))
    bist = input("Unesite tip bistabila (SR, JK, T, D): ").upper()
    d1 = {}
    d2 = {}
    print("Unesite kodove stanja:")
    for i in range(2 ** vars):
        s = input("Stanje S{:<2}: ".format(i)).upper()
        d1[s] = "S{}".format(i)
        d2["S{}".format(i)] = s
    
    # print(d)
    komb = []
    komb2 = []
    for s in sorted(d1):
        for j in range(2):
            ssi = input("S{:>2} {}: ".format(d1[s], j)).upper()
            komb.append(s + str(j) + d2[ssi.split(' ')[0]])
            komb2.append(int_to_binary(int(ssi.split(' ')[1]), 3))
        
    # print(komb)
    t = logicmin.TT(vars + 1, vars + vars * (bist in ['JK', 'SR']) + vars)
    for i in range(2 ** (vars + 1)):
        temp = ''
        for j in range(vars):
            temp += bist_pobuda(bist, komb[i][j], komb[i][-vars + j])
        t.add(komb[i][:vars + 1], temp + komb2[i])
        # print(komb[i], temp)
    
    # for k in komb: print(k)

    sols = t.solve()
    rj = str(sols)
    # print(rj)
    imena_varijabli = ['U']
    imena_varijabli.extend(['Q{}'.format(i, bist) for i in range(vars)])
    imena_izlaza = []
    for i in range(vars - 1, -1, -1):
        imena_izlaza.append('B{}.{}'.format(i, bist[0]))
        if bist == 'JK' or bist == 'SR':
            imena_izlaza.append('B{}.{}'.format(i, bist[1]))
    imena_izlaza.extend(['O{}'.format(i) for i in range(vars - 1, -1, -1)])
    

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
    automat()