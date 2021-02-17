text = input("add what you want in lowercase  : \n")
text_1 = text.split(". ")
for i in text_1:
    print(i.capitalize(), end=". ")

