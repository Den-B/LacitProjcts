number=int(input("Введите елемент для поиска: "))
listOfNumbers=[1,2,3,4,5,6,7,8,9,10,15.665,20,24,65,78.434,899,654,4445,342423.645,45354534,345566]
lenghtOfList = len(listOfNumbers)
def sequence(listOfNumbers,lenghtOfList,number):

    i = 0
    while i<lenghtOfList:
        if number==listOfNumbers[i]:
            print("Данный элемент есть в списке на "+str(i+1)+" позиции")
            break
        i+=1
    else:
            print("Этого элемента нет в списке.")
    l=0
    for i in listOfNumbers:
        if number==i:
            print("Данный элемент есть в списке на "+str(l+1)+" позиции")
            break
        l+=1  
    else:
        print("Этого элемента нет в списке.")



sequence(listOfNumbers,lenghtOfList,number)
