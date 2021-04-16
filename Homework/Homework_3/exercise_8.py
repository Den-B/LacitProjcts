ClassOfStudent = int(input("Введите класс студента: "))

def Students(ClassOfStudent):
    if ClassOfStudent < 0:
        print("Ошибка ввода.Ступень не найдена.")
    elif ClassOfStudent <=4:
        print("1 ступень ")
    elif ClassOfStudent <=9:
        print("2 ступень")
    elif ClassOfStudent <=11:
        print("3 ступень")
    else:
        print("Ошибка ввода.Ступень не найдена.")
Students(ClassOfStudent)
