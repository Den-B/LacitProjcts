ListOfEvenElements = [1,4,6,23,6,234,745,2,54532,674324,123,2,43221,5]
ListOfSets = list()
divider = int(input("Делитель: "))
setOfNumber = set()
setOfBul = set()
print("[ ")
for i in range(0,divider):
    for k in range(0,14):
        if ListOfEvenElements[k]%divider==i:
            setOfNumber.add(ListOfEvenElements[k])
    print(setOfNumber)
    setOfNumber.clear()
print(" ]\n\n") 
