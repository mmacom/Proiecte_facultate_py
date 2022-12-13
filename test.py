def patrat():
    n = int(input())
    print(n ** 2)


def lista():
   n =int(input())
   m =[]
   s =0
   for i in range(n):
       m.append(input())
       if (i<3) or (i>7):
           s +=int(m[i])
           print(m)
           print(s)

if__name__=="__main__":
      lista()


