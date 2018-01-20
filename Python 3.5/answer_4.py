def mult0(m,n):
    if n >0:
        return m + mult0(m,n-1)
    else:
        return 0

def mult(m,n):
    ans = 0
    while n>0:
        n = n-1
        ans = ans + m
    return ans

def even(n):
    return n%2 ==0

def fastmult0(m,n):
    if n>0:
        if even(n):
            return fastmult0(m+m,n//2)
        else:
            return m + fastmult0(m,n-1)
    else:
        return 0

def fastmult(m,n):
    ans = 0
    while n>0:
        if even(n):
            m = m + m
            n = n//2
        else:
            n = n-1
            ans = ans + m
    return ans

def russianmult0(m,n):
    if n > 1:
        if even(n):
            return russianmult0(m+m,n//2)
        else:
            return m + russianmult0(m+m,n//2)
    else:
        return m
    
def russianmult(m,n):
    ans = 0
    while n>1:
        if even(n):
            m = m+m
            n = n//2
        else:
            ans = ans + m
            m = m+m
            n = n//2

    return m + ans

def russianmult1(m,n):
    ans = 0
    while n>1:
        if not even(n):
            ans +=m
        m = m+m
        n = n//2
    return m + ans






            
    
