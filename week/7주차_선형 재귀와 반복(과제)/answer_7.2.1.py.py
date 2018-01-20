# // -> 정수 나눗셈


def even(n):
    return n%2 ==0

def odd(n):
    return n%2 ==1

def gcd(m,n):
    if not(m==0 or n==0):
        if even(m) and even(n):
            return 2* gcd(m//2,n//2)
        elif even(m) and odd(n):
            return gcd(m//2,n)
        elif odd(m) and even(n):
            return gcd(m,n//2)
        else:
            if m<= n:
                return gcd(m, (n-m)//2)
            else:
                return gcd(n,(m-n)//2)
            
    else:
        if m==0:
            return n
        else:
            return m
