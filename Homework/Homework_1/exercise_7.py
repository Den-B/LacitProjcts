ListOfEvenElements = [-2,57,345.324,-7854,32,67,45,-784,6,"ф"]
dictionary = dict()
i = 0
while i<=8:
    dictionary[ListOfEvenElements[i]]=ListOfEvenElements[i+1]
    i+=2

for key in dictionary:
    if dictionary[key]:
        print(dictionary[key])
print("\n\n")
