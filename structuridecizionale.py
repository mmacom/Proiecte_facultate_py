# de realizat o functie care verifica intr-un sir numarul de aparitii a cifrei 5
def sir5():
    print("Va rog introduceti un sir de numere naturale:")
    sir = input()
    print(sir)
    contor = 0
    for index in range(0,len(sir)):
        if int(sir[index]) == 5:
            contor += 1
        print("contor=", contor)

def lista5():
    print("Va rog introduceti un sir de numere naturale despartite prin spatiu:")
    lista = input().split(" ")
    print(lista)
    contor = 0
    for index in range(0, len(lista)):
          if int(lista[index]) == 5:
             contor += 1
    print("contor=", contor)

# de realizat o functie care preia un numar de tastatura si incadreaza acel numar in domeniile urmatoare
# 0 -> 3500 - mic
# 3500 -> 7000 - mediu
# 7000 -> - mare

def incadrare():
    print("Introduceti un numar:", end="")
    nr = int(input())
    if nr < 3500:
        print("mic")
    else:
        if nr<7000:
            print("mediu")
        else:
            print("mare")

# de realizat un meniu simplu, de genul
# Apasati tasta 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire
def adunare():
    print("a=", end="")
    a= int(input())
    print("b=", end="")
    b = int(input())
    print("a+b=", a+b)

def meniu():
    print("Apasati tasta 1 pentru adunare, 2 penru scadere, 3 pentru inmultire, 4 pentru inmultire ")
    o = input().strip()
    if o == "1":
        print("adunare")
        adunare()
    else:
        if o == "2":
            print("scadere")
            scadere()
        else:
            if o == "3":
               print("inmultire")
               inmultire()
            else:
                if o == "4":
                    print("impartire")
                    impartire()
def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b=", a-b)

def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b=", a*b)

def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b=", a/b)

if __name__ == "__main__":
    lista5()