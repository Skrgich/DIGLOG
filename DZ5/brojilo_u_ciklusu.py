import logicmin

def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]


def bistabil_pobuda(bis, poc, sljed):
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


def brojilo_u_ciklusu():
    d = {}
    print(' ')
    vars = int(input("Unesite broj bitova brojila: "))
    x = [int(s) for s in input("Unesite stanja ciklusa odvojena prazninom: ").split(', ')]
    if x[0] == x[-1]: x.pop()
    bistabil = input("Unesite tip bistabila ('D', 'T', 'SR', 'JK'): ").upper()
    for i in range(len(x)):
        d[int_to_binary(x[i], vars)] = int_to_binary(x[(i + 1) % len(x)], vars)
    
    for k in d:
        temp = ''
        for i in range(vars):
            temp += bistabil_pobuda(bistabil, k[i], d[k][i])
        d[k] = temp
    

    imena_varijabli = ['Q{}'.format(i) for i in range(vars)]
    imena_izlaza = []
    for i in range(vars - 1, -1, -1):
        imena_izlaza.append('{}{}'.format(bistabil[0], i))
        if bistabil == 'JK' or bistabil == 'SR':
            imena_izlaza.append('{}{}'.format(bistabil[1], i))

    t = logicmin.TT(vars, len(imena_izlaza))
    for k in sorted(d):
        t.add(k, d[k])
    
    sols = t.solve()
    rj = str(sols)

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