def gugudan1():
    for x in range(2,10):
        for y in range(1,10):
            if len(str(x*y)) ==2:
                print(str(x).rjust(2),"x",str(y).rjust(2),"=",str(x*y).rjust(1),end = '  ')
            else:
                print(str(x).rjust(2),"x",str(y).rjust(2),"=",str(x*y).rjust(2),end = '  ')
            if y % 3 ==0:
                print()
        print()

    
def gugudan2():
    for y in range(1,10):
        for z in range(2,6):
            if len(str(z*y)) == 2:
                print(str(z).rjust(2),"x",str(y).rjust(2),"=",str(z*y).rjust(1),end = '  ')
            else:
                print(str(z).rjust(2),"x",str(y).rjust(2),"=",str(z*y).rjust(2),end = '  ')
        print()
            
    print()
    
    for x in range(1,10):
        for k in range(6,10):
            if len(str(k*x)) == 2:
                print(str(k).rjust(2),"x",str(x).rjust(2),"=",str(k*x).rjust(1),end = '  ')
            else:
                print(str(k).rjust(2),"x",str(x).rjust(2),"=",str(k*x).rjust(2),end = '  ')
        print()
            
    
