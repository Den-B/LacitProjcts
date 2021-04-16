stringOne = input("Введите строку: ")
lenght = len(stringOne)
stringTwo = ""
i = 0

def Solve(lenght,i,stringTwo):
    while i<lenght:
        if  i<lenght-1 and stringOne[i+1]!=" " and stringOne[i].isdigit() and stringOne[i+1].isdigit()!=True  and  stringOne[i+1]!=")"and stringOne[i+1]!="}" and stringOne[i+1]!="]":
            stringTwo +=stringOne[i]
            stringTwo +=" "
        else:
            stringTwo=stringTwo+stringOne[i]
        i+=1
    print(stringTwo)

Solve(lenght,i,stringTwo)
