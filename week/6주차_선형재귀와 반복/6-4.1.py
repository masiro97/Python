def power(b,n):
    if n>0:
        if n%2 ==0:
            return power(b**2,n//2)
        else:
            return b * power(b,n-1)
    else:
        return 1
