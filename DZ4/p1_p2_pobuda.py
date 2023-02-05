from math import floor

def p1_p2_pobuda():
    p1 = list(map(float, input("Unesite parametre za P1: ").split(' ')))
    p2 = list(map(float, input("Unesite parametre za P2: ").split(' ')))

    p1_p2 = [floor(p1[0] / p2[1]), floor(p1[2] / p2[3])]
    p1_p2.append(min(p1_p2))
    p2_p1 = [floor(p2[0] / p1[1]), floor(p2[2] / p1[3])]
    p2_p1.append(min(p2_p1))

    for i in range(3):
        print("P1/P2 {:>2}: {:>3}".format('L' if i == 0 else 'H' if i == 1 else 'LH', p1_p2[i]))
    for i in range(3):
        print("P2/P1 {:>2}: {:>3}".format('L' if i == 0 else 'H' if i == 1 else 'LH', p2_p1[i]))


if __name__ == "__main__":
    p1_p2_pobuda()