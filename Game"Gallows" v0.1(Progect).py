import random

listOfWords = list()
listOfWords = ["водопад","дом","программирование","планета","герой","злодей"]
keyWord = ""
countOfMistakes = 0
countOfCorrectLetter = 0
countOfCorrectLetter = len(keyWord)
listOfLetters = []


def checkerOfLetters(listOfWords):
    global countOfCorrectLetter
    global countOfMistakes
    global listOfLetters
    global keyWord


    while countOfMistakes < 10 and countOfCorrectLetter != len(keyWord):

        letter = input("Введите букву: ")
        for k in keyWord:
            if k == letter:
                i = 0
                for j in keyWord:
                    if j ==letter and listOfLetters[i]!=j:
                        listOfLetters[i]= j
                        countOfCorrectLetter += 1
                    i+=1
                drawWord(listOfLetters)
                break
                
        else:
            countOfMistakes+=1
            draw(countOfMistakes,listOfLetters)

    else:
        checkerOfResults(countOfCorrectLetter,countOfMistakes)


def chosingWord(listOfWords):
    keyWord=random.choice(listOfWords)
    return keyWord

def draw(countofMistakes,listOfLetters):
    if countofMistakes == 1:
        print("                ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |   ")
        print("             |  ")
        print("                ")

    elif countofMistakes == 2:
        print("                ")
        print("    ---------|  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 3:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("    |        |  ")
        print("    |        |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 4:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 5:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("             |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 6:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("        |    |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 7:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("       /|    |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 8:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("       /|\   |  ")
        print("             |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 9:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("       /|\   |  ")
        print("        |    |  ")
        print("             |  ")
        print("                ")
    elif countofMistakes == 10:
        print("                ")
        print("    ---------|  ")
        print("    |        |  ")
        print("   | |       |  ")
        print("    -        |  ")
        print("        o    |  ")
        print("       /|\   |  ")
        print("        |\   |  ")
        print("             |  ")
        print("                ")

    else:
        checkerOfResults(countOfMistakes,0)
    drawWord(listOfLetters)

def drawWord(listOfLetters):
    print("Текущие открытые буквы: ",listOfLetters)


def checkerOfResults(countOfCorrectLetter,countOfMistakes):
    if countOfMistakes>=10:
        print("Вы проиграли.")
    elif countOfCorrectLetter == len(keyWord):
        print("Вы угадали слово: ",keyWord)



# #Accomplishment
keyWord = chosingWord(listOfWords)

for i in range(0,len(keyWord)):
 listOfLetters.append(" _ ")
print(drawWord(listOfLetters))

checkerOfLetters(listOfWords)


