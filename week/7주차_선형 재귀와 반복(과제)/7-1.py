def gcd(m,n):
    if n!=0:
        return gcd(n,m%n)
    else:
        return m
