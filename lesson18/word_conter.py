def word_counter(file_name: str) -> int:
    outfile = open(file_name, 'r', encoding='utf8')
    i = 0
    for line in outfile:
        for _ in line:
            i += 1
    return i


print(f"Всего символов в файле line.txt = {word_counter('line.txt')}")
