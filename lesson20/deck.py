import random


def shuffle(cards):
    random.shuffle(cards)
    print(f"Перетасованая колода: \n{cards}")


def take_cards(card_del, card):
    card.remove(card_del)
    return card


class Deck:
    def __init__(self, cards):
        self._card = cards

    def __str__(self):
        return f"Новая колода: \n{self._card}"


card_example = [('A', 'Spades'), ('K', 'Clubs'), (10, 'Diamonds'),
                (5, 'Hearts')]
deck = Deck(card_example)
shuffle(card_example)
print(f"Новая колода: {take_cards(('A', 'Spades'), card_example)}")
