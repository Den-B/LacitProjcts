N=int(input("Введите число в середине: "))

def OneToMax(N):
    if N > 0:
        for i in range(1,N+1):
            print(2*(N-i)*" ",end = " ")
            for j in range(1,i+1):
                print(j,end = " ")
            for j in range(i-1,0,-1):
                print(j,end=" ")
            print()

        for i in range(N-1,0,-1):
            print(2*(N-i)*" ",end = " ")
            for j in range(1,i+1):
                print(j,end = " ")
            for j in range(i-1,0,-1):
                print(j,end=" ")
            print()
    else:
        print("Error,number<0")
    
def MaxToOne(N):
    if N > 0:
        for i in range(1,N+1):
            print(2*(N-i)*" ",end = " ")
            for j in range(N,N-i,-1):
                print(j,end = " ")
            for j in range(N-i+2,N+1):
                print(j,end=" ")
            print()

        for i in range(N-1,0,-1):
            print(2*(N-i)*" ",end = " ")
            for j in range(N,N-i,-1):
                print(j,end = " ")
            for j in range(N-i+2,N+1):
                print(j,end=" ")
            print()
    else:
        print("Error,number<0")
OneToMax(N)
MaxToOne(N)
