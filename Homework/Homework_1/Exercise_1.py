ListOfEvenElements = [-2,57,345.324,-7854,32,67,45,-784,6,"ф"]
a=8
for i in range(0,10):
    if  (type(ListOfEvenElements[i]) == type(a) and ListOfEvenElements[i]%2==0 and ListOfEvenElements[i]>0):
            print(ListOfEvenElements[i])
print("\n\n")
