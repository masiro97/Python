#fibs = [0,1]
#fibs.append(fibs[1]+ fibs[0])
#fibs.append(fibs[2],fibs[1])

def fibseq(n):
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs
#마지막 원소 -> fibseq(40).pop()
