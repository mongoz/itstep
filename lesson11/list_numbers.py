lists = ['again', 'animal', 'point', '34', '-456', '678', '1', '2', '3', '4',
         'mother', 'world', 'near', 'build', 'self', 'earth', 'father']

new_list = list(map(int, filter(lambda x: x.isdigit(), lists)))

print(new_list)

# Почему-то не вернуло негативное число((
