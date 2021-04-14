a = 1
b = 1.1
listOfSum = list()
dictionary = {
    2:5342432,
    True:425423,
    "вфыфывфыв":False,
     634:432,
    False:425423,
    "лоапвфывфыв":False,
    "фыввфы":3223
    }

for key in dictionary:
    if (type(dictionary[key])==type(a) and type(key)==type(a)) or (type(dictionary[key])==type(b) and type(key)==type(a)):
        listOfSum.append(key+dictionary[key])
print(listOfSum)
print("\n\n")
