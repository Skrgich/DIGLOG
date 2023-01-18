def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]

def posmacni_mux():
    d = {}
    d2 = {
        '00': '0', '01': 'D', '10':'NOT D', '11': '1'
    }
    ans = []
    print(' ')
    vars = int(input("Unesite broj bitova brojila: "))
    x = [int(s) for s in input("Unesite stanja ciklusa odvojena prazninom: ").split(', ')]
    if x[0] == x[-1]: x.pop()
    stanja = x[:]

    for i in range(len(x)):
        d[x[i]] = int_to_binary(x[(i + 1) % len(x)], vars)[0]
    
    van_ciklusa = [i for i in range(2 ** vars) if i not in d]
    print("Unesite izlaze nespecifiranih stanja: ")
    for stanje in van_ciklusa:
        d[stanje] = input("Stanje {:2}: ".format(stanje))
        
    for i in range(0, 2 ** vars, 2):
        ans.append(d2[d[i] + d[i + 1]])
    print('')
    for i in range(len(ans)):
        print("D{:<2}={:>6}".format(i,ans[i]))
    print('\n')


def posmacni_dekoder():
    d = {}
    ans = []
    print(' ')
    vars = int(input("Unesite broj bitova brojila: "))
    x = [int(s) for s in input("Unesite stanja ciklusa odvojena prazninom: ").split(', ')]
    if x[0] == x[-1]: x.pop()
    
    for i in range(len(x)):
        d[x[i]] = int_to_binary(x[(i + 1) % len(x)], vars)[0]

    van_ciklusa = [i for i in range(2 ** vars) if i not in d]
    print("Unesite izlaze nespecifiranih stanja: ")
    for stanje in van_ciklusa:
        d[stanje] = input("Stanje {:2}: ".format(stanje))

    for i in range(2 ** vars):
        if d.get(i) ==  '1': ans.append(i)
    
    print(' ')
    print(', '.join([str(c) for c in ans]))
    print('\n')

if __name__ == "__main__":
    print("  \nUnesite inacicu zadatka\nM za inacicu s multipleksorom\nD za inacicu s dekoderom")
    inacica = input()
    if inacica.lower() == 'm': posmacni_mux()
    elif inacica.lower() == 'd': posmacni_dekoder()
