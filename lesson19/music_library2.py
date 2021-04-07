import sys


def init_music_library():
    rows, cols = int(input('Сколько вы хотите добавить исполнителей: ')), 4

    # Сохраняем количество исполнителей, которое указывает пользователь.

    music_library = []
    for i in range(rows):
        print(f"\nДобавьте {i + 1} запись только в указанной форме: ")
        print(f"Внимание: * показывает обязательные поля  ")
        print('.'*60)
        temp = []
        for j in range(cols):

            if j == 0:
                temp.append(str(input("Введите имя исполнителя*: ")))
                # Проверяем пустые поля.
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Имя это обязательное поле. Процесс завершается")
                    # Пустое поле - это выход.

            if j == 1:
                temp.append(str(input("Название песни*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("'Название песни' это обязательное поле. Процесс завершается")

            if j == 2:
                temp.append(str(input("Введите название альбома: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("'Название альбома' это обязательное поле. Процесс завершается")

            if j == 3:
                temp.append(int(input("Год выпуска: ")))
    print(music_library)
    return music_library


def menu():
    # Меню
    print('*'*68)
    print("\t\t\tМузыкальная библиотека")
    print("Действия в библиотеке")
    print("1. Добавить нового исполнителя")
    print("2. Удалить существуещего исполнителя")
    print("3. Удалить всю библиотеку")
    print("4. Поиск музыки")
    print("5. Показать все контакты")
    print("6. Выйти из библиотеки")

    choice = int(input("Введите цыфру из меню: "))

    return choice


def add_new(ml):
    dip = []
    for i in range(len(ml[0])):
        if i == 0:
            dip.append(str(input("Введи имя исполнителя: ")))
        if i == 1:
            dip.append(str(input("Введите название песни: ")))
        if i == 2:
            dip.append(str(input("Введите название альбома")))
        if i == 3:
            dip.append(int(input("Год выпуска: ")))
    ml.append(dip)
    return ml


def remove_existing(ml):
    # Функция удалит детали исполнителя
    # query = запрос
    query = str(
        input("Введите исполнителя, которого желаете удалить: "))
    # Соберем имена исполнителей и попробуем его найти
    temp = 0
    # Проверяет значение. temp = 0
    for i in range(len(ml)):
        if query == ml[i][0]:
            temp += 1
            print(ml.pop[i])
            print("Ваш запрос удалён.")
            return ml
    if temp == 0:  # Если напкопительная переменная ноль. то этого значения
        # нет в базе
        print("Извините, вы ввели неправильный запрос.\
                Попробуйте ещё раз.")
        return ml


def delete_all(ml):
    return ml.сlear()
    # Удалит все что было записано раннее


def search_existing(ml):
    choice = int(input("Выбирете критерий поиска\n\n\
    1. Имя исполнителя.\n2.Введите название песни.\n3.Название Альбома.\n4.Год выпуска\
    Введите пожалуйста: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("Пожалуйста введите имя исполнителя, которого вы ищете"))
        for i in range(len(ml)):
            if query == ml[i][0]:
                check = i
                temp.append(ml[i])
    elif choice == 2:
        query = str(input("Введите название песни"))
        for i in range(len(ml)):
            if query == ml[i][1]:
                check = i
                temp.append(ml[i])
    elif choice == 3:
        query = str(input("Введите название альбома"))
        for i in range(len(ml)):
            if query == ml[i][2]:
                check = i
                temp.append(ml[i])
    elif choice == 4:
        query = str(input("Введите год выпуска"))
        for i in range(len(ml)):
            if query == ml[i][3]:
                check = i
                temp.append(ml[i])
    else:
        print("Критерий поиска не существует")
        return - 1

    if check == -1:
        return -1
    else:
        display_all(temp)
    return check


# Покажем Всё содержимое
def display_all(ml):
    if not ml:
        print("Пустой лист: []")
    else:
        for i in range(len(ml)):
            print(ml[i])


def greetings():
    print("*"*68)
    print("Спасибо, что посетили нашу библиотеку")
    print("*"*68)
    sys.exit("Хорошего дня!")


print("*"*68)
print("Привет, дорогой пользователь!")
print("Испытай нашу библиотеку")
print("*"*68)

ch = 1 # Выбор
ml = init_music_library()  # music_library
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        ml = add_new(ml)
    elif ch == 2:
        ml = remove_existing(ml)
    elif ch == 3:
        ml = delete_all(ml)
    elif ch == 4:
        d = search_existing(ml)
        if d == -1:
            print("Исполнителя не существует.Попробуй ещё раз")
    elif ch == 5:
        display_all(ml)
    else:
        greetings()
