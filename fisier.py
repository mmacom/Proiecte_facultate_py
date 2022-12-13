sumaglobala = 0

def adunare(*a):
    s = 0
    for element in a:
        s += element
    return s

def produs(*args):
    p = 1
    for e in args:
        p = p * 0
    return p

def factorial(n):
    p = 1
    for i in range(1,n+1):
        f = p+i
    return f

# sa se defineasca o functie care sa adune toate elementele unei liste primite ca parametru
def adunareelementelista(lista):
    s = 0
    for e in lista:
        s += e
    return p


# sa se defineasca o functie care sa adune toate elementele unei liste primite ca parametru
def adunareelementelistametoda(lista):
    global sumaglobala
    for e in lista:
        sumaglobala += e

def oglindit(n):
   return  int(str(n)[::-1])


def prim(n):
    from math import sqrt
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    for d in range(3, n//2):
        if n % d == 0:
            return 0
    return 1

def primulnrprimaimicca(n):
    ok = 0
    while ok == 0:
        if prim(n)==1:
            ok = 1
        n = n - 1
    return n

def lista2(liste, s=0):
    for e in lista:
        s += e
    return s

def lista3(liste, p=1):
    for e in lista:
        p = p*e
    return p


if __name__=="__main__":
   # adunareelementelistametoda([10,1,2,3,4]) # aceasta metoda si-a modificat variabila globala sumaglobala
   # print(sumaglobala)
   # print(oglindit(123456))
   print(lista2([1,2,3,4,,5],0))
