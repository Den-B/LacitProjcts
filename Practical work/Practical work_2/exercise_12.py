number=int(input("Введите елемент для поиска: "))
listOfNumbers=[1,2,3,4,5,6,7,8,9,10,15.665,20,24,65,78.434,899,654,4445,342423.645,45354534,345566]
lenghtOfList = len(listOfNumbers)
i = 0
while i<lenghtOfList:
    if number==listOfNumbers[i]:
        print("Данный элемент есть в списке на "+str(i+1)+" позиции")
        break
    i+=1
    
else:
    print("Этого элемента нет в списке.")
