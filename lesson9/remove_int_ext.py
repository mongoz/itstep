def delete_function(values_list, num):
    total = 0
    while num in values_list:
        values_list.remove(num)
        total += 1
    print(f"Удалено элементов из списка:{total}. "
          f"Это элемент:{num}")


array = [1, 2, 3, 4, 5, 6, 7, 8, 4, 4, 4]
delete_function(array, 6)

