def brojilo_s_memorijom():
    d = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    ans = []
    print(' ')
    vars = int(input("Unesite broj bitova brojila: "))
    x = [int(s) for s in input("Unesite stanja ciklusa: ").replace('->', ' ').replace(',', ' ').split(' ') if s]
    sljed = {}
    for i in range(len(x)):
        sljed[x[i]] = x[(i + 1) % len(x)]

    memorija = [[None for j in range(2 ** (vars - 1))] for i in range(2)]
    for i in range(2):
        for j in range(2 ** (vars - 1)):
            memorija[i][j] = d[sljed[i * 2 ** (vars - 1) + j]] if sljed[i * 2 ** (vars - 1) + j] in d else str(sljed[i * 2 ** (vars - 1) + j])
    
    print('')
    for i in range(2):
        for j in range(2 ** (vars - 1)):
            print("R{} {}: {}".format(i + 1, j, memorija[i][j]))
        print('')
    print('')





if __name__ == "__main__":
    brojilo_s_memorijom()