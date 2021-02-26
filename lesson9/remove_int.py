def delete_function(list_values, num):
    clear_array = []
    for x in list_values:
        if x == num:
            continue

        clear_array.append(x)
    return clear_array


array = [1, 2, 3, 4, 5, 6, 7, 8, 4, 4, 4]
print(delete_function(array, 4))
