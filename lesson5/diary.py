
day = int(input("Enter the day \n"))
task = [

    "Monday go for a walk; read the book",
    "Tuesday meet friend Andrew at 5 p.m; go to the gym",
    "Wednesday do homework; play 'UFC:3'",
    "Thursday go for a walk; read the book",
    "Friday meet friend Andrew; at 5 p.m go to the gym",
    "Saturday do homework; play 'UFC:3'",
    "Sunday go for a walk; read the book"
]
if day in range(0, 8):
    print(f"{task[day]}")
