from time import time
from threading import Thread
import os
import random
import json
# Actualised a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def create_file_of_numbers(quantity=10000,
                           filename='random_numbers.json') -> str:
    """
    created new file of numbers and return name of file
    """
    start_time = time()
    with open(filename, "w") as f:
        dates = []
        for _ in range(quantity):
            dates.append(random.randint(-99, 99))
        json.dump(dates, f, indent=4)
    finish_time = time()
    spent_time = finish_time - start_time
    print(f"a new file '{filename}' of {quantity} numbers has been created")
    print(f"spent time {spent_time}")
    return filename


def splitting_the_file_with_numbers(filename, number_sign):
    """
    splitting the file of numbers
    """
    new_filename = os.path.join(os.path.dirname(filename),
                                f"{number_sign}_"
                                f"{os.path.basename(filename)}")
    start_time = time()
    with open(filename, "r") as f:
        load_dates = json.load(f)
    with open(new_filename, "w") as f:
        save_dates = []
        for i in load_dates:
            if (i > 0 and number_sign == 'positive') or (
                    i < 0 and number_sign == 'negative'):
                save_dates.append(i)
        json.dump(save_dates, f, indent=4)
    finish_time = time()
    spent_time = finish_time - start_time
    print(f"\nA new file '{new_filename}' of "
          f"{len(save_dates)} {number_sign} numbers has been created"
          f"\nspent time {spent_time}")


if __name__ == "__main__":
    print("All the best to you!")
    print("Welcome to the multi-threaded sorter MTS-1!")
    print("If you have a file with numbers,")
    print("enter the name of this file or enter nothing")
    while True:
        path = input("Enter the name of a file with numbers: ")
        if path:
            try:
                with open(path, "r") as f:
                    data = f.readline()
                break
            except FileNotFoundError:
                print('You made a mistake')
        else:
            filename = create_file_of_numbers()
            break
    if input("Start sorting? y/n ") == 'y':
        time_ch = time()
        t1 = Thread(target=splitting_the_file_with_numbers,
                    args=(filename, 'positive'))
        t1.start()
        print("Creating a file with positive numbers started!")
        t2 = Thread(target=splitting_the_file_with_numbers,
                    args=(filename, 'negative'))
        t2.start()
        print("Creating a file with negative numbers started!")
        t1.join()
        t2.join()
        time2 = time()
        print(f"\nTotal execution time {time2 - time_ch}")

    print("\nGoodbye!")