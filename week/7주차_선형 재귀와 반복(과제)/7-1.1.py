def gcd2(m,n):
    if m!=0 and n!= 0:
        if m %2 ==0 and n %2 ==0:
            return 2*gcd2(m/2,n/2)
        elif m%2 ==0 and n%2 !=0:
            return gcd2(m/2,n)
        elif m%2 !=0 and n%2 ==0:
            return gcd2(m,n/2)
        else:
            if m<=n:
                return gcd2(m,(n-m)/2)
            else:
                return gcd2(n,(m-n)/2)
            
    elif m==0 and n!=0:
        return int(n)
    elif n==0 and m!= 0:
        return int(m)
    else:
        return 0
