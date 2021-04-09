
big_basket = {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2,
    'meat': 2.4,
    'eggs': 0.4,
    'fish': 2.4

}


def find_most_in_food_basket(food_basket, max_cost):
    key_list = []
    if max_cost:
        for value in food_basket:
            if food_basket[value] > 2:
                key_list.append(value)

        key_set = set(key_list)
        return key_set

    else:
        if not max_cost:
            for value in food_basket:
                if food_basket[value] < 1:
                    key_list.append(value)

            key_set = set(key_list)
            return key_set


print(find_most_in_food_basket(big_basket, max_cost=True))
print(find_most_in_food_basket(big_basket, max_cost=False))

