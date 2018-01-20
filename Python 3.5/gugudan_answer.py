def gugudan1():
    for i in range(2,10):
        for j in range(1,10):
            if j % 3 == 0 :
                print(i,"x",j,"=",str(i*j).rjust(2))
            else:
                print(i,"x",j,"=",str(i*j).rjust(2),end = '  ')
        print()


def gugudan2():
    for k in [2,6]: # range(2,7,4)
        for i in range(1,10):
            for j in range(k,k+4):
                print(j,"x",i,"=",str(j*i).rjust(2), end = '  ')
            print()
        print()
