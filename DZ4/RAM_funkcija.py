def RAM_funkcija():
    d = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    x = [int(s) for s in input("Unesite stanja ciklusa: ").replace('(', '').replace(')', '').replace('P=','').replace(',', ' ').split(' ') if s]
    redoslijed = input("Unesite redoslijed ulaza mux-a (01 ili 10): ")
    if redoslijed == "01":
        for i in range(0, 16, 2):
            print("Lokacija {}: {}{}".format(i // 2, d.get(x[i], x[i]), d.get(x[i + 1], x[i + 1])))
    else:
        for i in range(0, 16, 2):
            print("Lokacija {}: {}{}".format(i // 2, d.get(x[i + 1], x[i + 1]), d.get(x[i], x[i])))
       


if __name__ == "__main__":
    RAM_funkcija()