stringForExample = input("Введите строку: ")
def Code(stringForExample):
    for i in stringForExample:
        print(ord(i),end=",\t")
    summa = 0
    for i in stringForExample:
        summa+=ord(i)
    print(summa)

Code(stringForExample)
