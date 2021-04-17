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
    print("                ")#1

    if countofMistakes == 1:#2
        print("             |  ")
    else:
        print("    ---------|  ")

    if countofMistakes<=2:#3
        print("             |  ")
    else:
        print("    |        |  ")

    if countofMistakes <=2:#4
        print("             |  ")
    elif countofMistakes ==3:
        print("    |        |  ")
    else:
         print("   | |       |  ")

    if countofMistakes <=2:#5
        print("             |  ")
    elif countofMistakes ==3:
        print("    |        |  ")
    else:
        print("    -        |  ")

    if countofMistakes <=4:#6
        print("             |  ")
    else:
        print("        o    |  ")

    if countofMistakes <=5:#7
        print("             |  ")
    elif countofMistakes ==6:
        print("        |    |  ")
    elif countofMistakes ==7:
        print("       /|    |  ")
    else:
        print("       /|\   |  ")

    if countofMistakes <=8:#8
        print("             |  ")
    elif countofMistakes ==9:
        print("        |    |  ")
    else:
        print("        |\   |  ")

    print("             |  ")#9
    
    print("                ")#10

  
    if countOfMistakes == 10:
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
print("Игра: Висельница.\nВаша задача: вводить любые буквы.\nЕсли вы угадали,то буква будет выведена,в ином случае картинка будет дополнена новым элементом.\nВсего допустимо 9 ошибок.")
print("Версия:1.2.")

keyWord = chosingWord(listOfWords)
for i in range(0,len(keyWord)):
 listOfLetters.append(" _ ")
drawWord(listOfLetters)

checkerOfLetters(listOfWords)




