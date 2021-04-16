dictionary = {
    10:"Ten",
    1:"One",
    3:"Three",
    2:"Two",
    5:"Five",
    9:"Nine",
    4:"Four",
    6:"Six",
}

def dictionaryOfNumbers():
    listOfKeys=list(dictionary.keys())
    listOfKeys.sort()
    for i in listOfKeys:
        print(i,":",dictionary[i])
dictionaryOfNumbers(dictionary)
