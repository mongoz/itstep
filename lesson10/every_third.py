def every_third():
    even_list_generate()


def even_list_generate():
    num1 = int(input("Введите число начала диапазона:\t"))
    num2 = int(input("Введите число конца диапазона:\t"))
    a = []
    for i in range(num1, num2+1, 3):
        a.append(i)
    print("-"*40)
    print(f"Генерация списка в диапазоне от\t{num1} до {num2}")
    print(a)


every_third()