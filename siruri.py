def inlocuire():
    sir = input()
    sirnou = ""
    for caracter in sir:
        if caracter in 'aeiou':
            sirnou += caracter.upper() # sirnou = sirnou + caracter . upper()
            print(caracter.upper())
        else:
            sirnou += caracter # sirnou = sirnou + caracter
            print(caracter)
    print(sirnou)

def schimbarecuvint():
    cuvint = input()
    index = 0
    cuvintnou = ""
    for caracter in cuvint:
        if index == 0:
           cuvintnou += caracter.upper()
           print(caracter.upper()," am gasit primul element ",index)
        else:
           if index == len(cuvint)-1:
              cuvintnou += caracter.upper()
              print(caracter.upper(),"am gasit ultimul element", index)
           else:
               print(caracter, index)
        index += 1


def halfsort():
    liste = [ 34, 0, 2, 5, 3,300, 56]
    print(liste)
    jumatate = len(liste) // 2
    print(len(liste),jumatate)
    list1 = liste[:jumatate:]
    print(liste)
    list1.sort()
    print(liste)
    liste2 = liste[jumatate::]
    print(liste2)
    liste,sort()
    print(liste)


if __name__ == "__main__":
   halfsort()