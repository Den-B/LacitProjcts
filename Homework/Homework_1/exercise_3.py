ListOfEvenElements = [-2,57,345.324,-7854,32,67,45,-784,6,"ф"]
a = 8
b = 2.4
for i in range(0,9):
    if  (type(ListOfEvenElements[i]) == type(a) or type(ListOfEvenElements[i]) == type(b)) and ListOfEvenElements[i]>0:
            print(ListOfEvenElements[i])
print("\n\n")
