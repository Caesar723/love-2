
def love(n):
    for a in range(0,round(n/2+0.1)-1):
        for b in range(0,round(n/2+0.1)-1-a):
            print(" ",end="")
        if n%2==0:
            for c in range(0,2+2*a):
                print("*",end="")
        else:
            for f in range(0,1+2*a):
                print("*",end="")
        for d in range(0,(round(n/2+0.1)-1-a)*2-1):
            print(" ",end="")
        if n%2==0:
            for c in range(0,2+2*a):
                print("*",end="")
        else:
            for f in range(0,1+2*a):
                print("*",end="")
        print()
    for g in range(0,n):
        for h in range(0,g):
            print(" ",end="")
        for i in range(0,2*n-1-2*g):
            print("*",end="")
        print()
love(5)
