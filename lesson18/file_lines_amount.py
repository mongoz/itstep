def lines_count(file_name: str):
    file_name = open('line.txt', 'r', encoding='utf-8')
    line = file_name.readline()
    count_lines = 0
    count_none_filled_lines = 0

    while line != '':
        line.rstrip('\n')
        line = file_name.readline()
        count_lines += 1
        if line == '':
            count_none_filled_lines += 1

    sum_of_filled_lines = count_lines - count_none_filled_lines
    return sum_of_filled_lines


print(f"Cумма заполненых (непустых) ячеек в файле = {lines_count('line.txt')}")


#  \n ''
