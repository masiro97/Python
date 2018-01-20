def mult1(m,n):
    if (n>0):
        return m + mult1(m,n-1)
    else:
        return 0


def mult0(m,n):
    ans = 0
    while n >0:
        ans = ans + m
        n = n-1
    return ans
        
    
def fastmult(m,n):
    if n >0:
        if (n % 2  ==0):
            return fastmult(m+m,n//2)
        else:
            return m + fastmult(m,n-1)
    else:
        return 0

def fastmult0(m,n):
    ans = 0
    while(n>0):
        if n % 2 == 0:
            m = m + m
            n = n//2
        else:
            ans =  ans  + m
            n = n-1
    return ans

def russian_mult(m,n):
    if n!=1:
        if (n%2 !=0):
            return m + russian_mult(m*2,int(n//2))
        else:
            return russian_mult(m*2,n//2)
    else:
        return m
            
            

def russian_mult0(m,n):
    if (n %2 !=0):
        total = m
    else:
        total = 0
    while (n !=1):
        m = m*2
        n = int(n//2)
        if (n % 2 ==1):
            total = m + total
    return total

