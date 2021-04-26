n=int(input("Введите число n: "))
for k in ((x,y) for x in range(1,n)  for y in range(1,n)):
    if k[0]<k[1]:
        print(k)
