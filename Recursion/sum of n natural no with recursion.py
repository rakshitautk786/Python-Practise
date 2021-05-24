def sun_recur(n):
    s=0
    if n==0:
        s+=0
        return s
    else:
        s=n+sun_recur(n-1)
        return s
n=int(input())
print(sun_recur(n)) 