n=int(input(" Enter "))
for i in range(n):
    print(" "*(n-i-1),end="")
    print(' '.join(str(11**i)),end="")
    print(" "*(n-i-1))
