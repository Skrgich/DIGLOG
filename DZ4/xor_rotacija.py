
def xor_rotacija():

    dhex = {
        10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }

    print("Unesite tip posmaka broja n: \n(a - aritmeticki)\n(l - logicki)\n(k - kruzni)")
    posmak = input()
    print("Unesite broj mjesta posmaka: ")
    k = int(input())
    print("unesite smjer posmaka (L ili D): ")
    smjer = input().lower()
    d = {}
    memorija = [0 for _ in range(8)]
    for i in range(16):
        d[i] = i
        for _ in range(k):
            if posmak == 'a' and smjer == 'd':
                d[i] = d[i] // 8 * 8 + d[i] // 2
            elif posmak == 'a':
                d[i] = d[i] // 8 * 8 + (d[i] * 2) % 8
            elif posmak == 'l' and smjer == 'd':
                d[i] = d[i] // 2
            elif posmak == 'l':
                d[i] == (d[i] * 2) % 16
            elif posmak == 'k' and smjer == 'd':
                d[i] = d[i] % 2 * 8 + d[i] // 2
            elif posmak == 'k':
                d[i] = d[i] // 8 + (d[i] * 2) % 16


        d[i] = i ^ d[i]
        for j in range(4):
            memorija[i // 2] += ((d[i] // (2 ** j)) % 2) * (2 ** (2 * j + 1 - i % 2))

            
    for i in range(8):
        print("Lokacija {}: {}{}".format(i, dhex.get(memorija[i] // 16, memorija[i] // 16), dhex.get(memorija[i] % 16, memorija[i] % 16)))
       




if __name__ == "__main__":
    xor_rotacija()