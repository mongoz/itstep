basket_example = {
    "bread": 1.2,
    "milk": 1.6,
    "potato": 0.4,
    "sunflower": 2,
    "meat": 2.4,
}


def calculate_food_basket(food_basket: dict, exchange_rate: float) -> float:
    total_price = 0
    for i in food_basket:
        total_price += food_basket[i]
    total_exchange = total_price * exchange_rate
    return total_exchange

# можно ещё через total = sum(food_basket.values())*exchange_rate  return total


print(f"Цена с конвертацией ${calculate_food_basket(basket_example, 27.5):.1f}")



