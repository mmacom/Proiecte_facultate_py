def matrice1():
    n = 4
    sdp = 0
    sds = 0
    matrice = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] =int(input())
            if i < j: # elementul este deasupra d p.
               sdp += matrice[i][j]
            if i+j < n-1: # elementul este deasupra d s.
               sds += matrice[i][j]
    print("SDP=",sdp)
    print("SDS=",sds)


def matrice2():
    m = 2 #coloane
    n = 2 #randuri
    matrice =[[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]**2

def matrice3():
     m = 2  # coloane
     n = 2  # randuri
     matrice = [[0] * n for _ in range(m)]

     for i in range(m):
         for j in range(n):
             matrice[i][j] = int(input())
             matrice[i][j] = matrice[i][j] ** 10


def caut100():
    n = 10
    lista = []
    print(lista)
    for i in range(n):
        lista.append(int(input()))

    for i in range(n):
        if lista[i] == 100:
            print(i)


def cauta100():
    #cauta 100 in matrice
    n = 2 #randuri
    m = 2 #coloane
    print(matrice)
    for i in range(n):
        matrice.append(int(input()))

    for i in range(m):
        if matrice[i][j] == 100:
            print(i)

def suma_elementelor():
    n = 2
    sdp = 0
    sds = 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(i, '', j, end='=')
            matrice[i][j] = int(input())
            if i < j:
                sdp += matrice[i][j]
            if i+j < n-1:
                sds += matrice[i][j]
    print('Suma d p =', sdp)
    print('Suma d s=', sds)

def sumpare():
    n = 2
    suma = 0
    matrice = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i // 2 == 0:
                suma += matrice[i][j]
    print("suma pare=" , suma)


if __name__== "__main__":
    sumpare()



