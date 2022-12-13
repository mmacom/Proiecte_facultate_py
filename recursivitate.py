def cautaresir(sirprincipal, subsir):
    i = 0 # indice pentru parcurgerea sirului principal
    n = len(sirprincipal) - len(subsir) # cat de mult din sirul principal are sens sa parcurg
    while i<=n:
        j = 0
        flg = True
        while flg and j<len(subsir):# verific daca sirul meu il gasesc in sirul principal. Daca difera ceva ies afara deoarece nu
                                    # are sens sa merg mai departe
            if sirprincipal[i+j]!=subsir[j]:
                flg = False
            j = i + 1
        # daca din while-ul precedent s-a iesit cu flg == True inseamna ca e posibil ca sirul meu sa fi fost gasit
        # daca j == lungimea sirului meu atunci sigur am gasit potrivirea sa pot iesi din functie
        if flg and j==len(subsir):
            return 1
        #ma mut in sirul principal cu valoarea lui j pentru ca nu am gasit potrivire
        i = i + 1
    return -1


# doresc o functie care aduna numerele naturale pana la n
# 1 + 2 + 3 + 4 + 5
def adunare(n):
    s = 0
    i = 1
    while i<=n:
        s = s + i
        i = i + 1
    return s


def factrec(n): # adunare(5) = 5 + adunare(4)
                # adunare(4) = 4 + adunare(3)...
    if n<=1:
        return 1
    else:
        return n * factrec(n - 1)

def fib(n): # al n-lea termen in sirul lui Fibonacci
    s = 0
    i = 0
    while i<n:
        if i == 0:
           t1 = 0
        else:
           t1 = t2
        if i == 1:
            t2 = 1
        else:
           t2 = s
        s = t1 + t2
        i = i + 1
    return s

def nr_cifre(n):
    c = 0
    if str(n)[len(str(n))-1]=='0':
        c = 1
        if len(str(n)) - 1 < 0:
            return c
    return c + nr_cifre(int(str(n))-1]))

if __name__=="__main__":
   print(nr_cifre(2000))