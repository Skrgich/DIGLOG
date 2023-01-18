def brojilo_u_standardno():
    d = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    ans = []
    print(' ')
    vars = int(input("Unesite broj bitova brojila: "))
    x = [int(s) for s in input("Unesite stanja ciklusa: ").replace('->', ' ').replace(',', ' ').split(' ') if s]

    print('')
    for i in range(2 ** (vars)):
        print("{:>3}.  {}".format(i, d[x.index(i)] if x.index(i) in d else x.index(i)))
    print('\n')




if __name__ == "__main__":
    brojilo_u_standardno()