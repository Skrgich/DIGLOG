def int_to_binary(integer, size):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return ('000000' + binary_string)[-size:]


def CLB_FPGA():

    vars = int(input("\nUnesite broj ulaza: "))
    funkcija = input("Unesite funkciju: ")

    print('')
    for i in range(2 ** vars):
        
        temp = funkcija.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
        vr = int_to_binary(i, vars)
        for j in range(vars):
            temp = temp.replace(chr(65 + j), vr[j]) 
        
        print("D{:<2}: {}".format(i, eval(temp)))
    print('\n')


if __name__ == "__main__":
    CLB_FPGA()
