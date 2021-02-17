first_list = ['Neo', 'Trinity', 'Mouse']
second_list = ['Matrix', 'Forever', 'Alone']
output_list =[]
if len(second_list) != len(first_list):
    print('list length mismatch')
else:
    for each in range(0, len(second_list)):
        output_list.append(first_list[each] + str(second_list[each]))

