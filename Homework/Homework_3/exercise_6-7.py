N=int(input("Введите число N: "))

def compare(N):
    Ncount = N
    difN = 1
    while Ncount >= 10:
        Ncount=Ncount/10
        difN+=1
    return difN

def oneToN(dif):
    if N > 0:
        for i in range(1,N+1):
            print((dif+1)*((N-i))*" ",end = "")
            for j in range(1,i+1):
                print((dif-compare(j))*" ",j,end="")

            for j in range(i-1,0,-1):
                print((dif-compare(j))*" ",j,end="")
            print()

        for i in range(N-1,0,-1):
            print((dif+1)*((N-i))*" ",end = "")
            for j in range(1,i+1):
                print((dif-compare(j))*" ",j,end="")
            for j in range(i-1,0,-1):
                print((dif-compare(j))*" ",j,end="")
            print()
    else:
         print("Error,number<0")
    print("\n\n\n\n\n")

def nToOne(dif):
    if N > 0:
        for i in range(1,N+1):
            print((dif+1)*((N-i))*" ",end = "")
            for j in range(N,N-i,-1):
                print((dif-compare(j))*" ",j,end="")
            for j in range(N-i+2,N+1):
                print((dif-compare(j))*" ",j,end="")
            print()

        for i in range(N-1,0,-1):
            print((dif+1)*((N-i))*" ",end = "")
            for j in range(N,N-i,-1):
                print((dif-compare(j))*" ",j,end="")
            for j in range(N-i+2,N+1):
                print((dif-compare(j))*" ",j,end="")
            print()
    else:
        print("Error,number<0")
    print("\n\n\n\n\n")

dif = compare(N)
oneToN(dif)
nToOne(dif)
