def sum(s):
    if s > 0:
        return s + sum(s-1)
    else:
        return 0


def sumrange(m,n):
    if m <= n:
        sum_n = sum(n)
        sum_m = sum(m-1)
        return sum_n - sum_m

    else:
        return 0
