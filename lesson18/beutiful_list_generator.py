
def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    infile = open(file_name, 'w', encoding='utf-8')
    for i in lst:
        infile.write(f"{marker} {i}\n")
    return True


if __name__ == '__main__':
    dc_heroes = ["Batman",
                 "Superman",
                 "Flash",
                 "Green Lantern",
                 "Wonder Woman"]

    beautiful_list_generator(dc_heroes, '\u2713', 'heroes.txt')

