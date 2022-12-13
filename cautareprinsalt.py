def cautare_salt():
    l = [2, 3, 7, 10, 12, 50, 67, 8, 77, 82, 97,4, 19, 100]
    l.sort()
    n =len(l)
    salt = int(math.sqrt(n))
    val = int(input()) # 60
    # identificam portiunea/bucata de lista in care se gaseste valoarea cautata.
    # st si st+salt
    for i in range(0, n, salt):
        if l[i]< val:
            st = i
        elif l[i] == val:
            print(i)
        else:
            break
# efectuez o cautare secventiala pe bucata de lista identificata anterior
  for i in range(st, st+salt):
      if l[i] == val:
          print(i)


if__name__=="__main__":
   cautare_salt()


