n=int(input("Введите число n: "))
def funct(n,*tupleI):
    for i in range(1,n+1):
        if n%i==0:
            yield i

gen =  funct(n)
for k in range(1,n+1):
    print(next(gen))
