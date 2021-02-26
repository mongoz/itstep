# Напишіть програму months.py яка чекає від
# користувача введення числа від 1 до 12 та у відповідь
# друкує назву місяця англійською. Наприклад, якщо
# було введено 2 програма виведе February. Якщо
# користувач ввів дані які не відповідають числу в
# діапазоні від 1 до 12, програма виведе повідомлення
# You made a mistake, repeat with numbers from 1
msg = "You made a mistake, repeat with numbers from 1 to 12"
a = ("December", "January", "February",
     "March", "April", "May",
     "June", "July", "August",
     "September", "October",
     "November")
b = int(input("Enter number of month\n"))
if b <= 12:
    print(a[b])
else:
    print(msg)
