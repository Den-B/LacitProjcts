n=int(input("Введите число n: "))
def gener_3(n):
    count = 0
    for k in ((x,y) for x in range(1,n)  for y in range(1,n)):
        if k[0]<k[1]:
            yield k
            count+=1
            if count ==2:
                break
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            if count>2:
                yield i

gen =  gener_3(n)
for k in range(1,n):
    print(next(gen))
    
