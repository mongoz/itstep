import json
shopping_list_example = [
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower oil": 2,
        "meat": 2.4

    },
    {
        "bread": 1.2,
        "milk": 1.6,
        "potato": 0.4,
        "sunflower": 2,
        "meat": 2.4,
        "eggs": 0.4,
        "fish": 2.4
    }
]

with open('shopping_list.json', 'w', encoding='utf8') as outfile:
    json.dump(shopping_list_example, outfile)
