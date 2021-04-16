def compareOfNumbers(a,b):
    if a > b:
        print("\nПервое больше второго.")
    elif a < b:
        print("Второе больше первого.")
    else:
        print("Они равны")
    print("\n\n")
    
def inputNumbers():
    af = float(input("Введите первое целое число: "))
    bf = float(input("Введите первое целое число: "))

    ai = int(af)
    bi = int(bf)
    compareOfNumbers(af,bf)
    compareOfNumbers(ai,bi)
inputNumbers()
