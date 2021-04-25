import random


class Deck:
    def __init__(self, cards):
        self._card = cards

    def shuffle(self, cards):
        random.shuffle(cards)
        print(f"Перетасованая колода: \n{cards}")

    def take_cards(self, card_del, card):
        for i in range(0, len(self._card)):
            if card_del == i:
                card.remove(card_del)
                print(f'Новая колода: {self._card}')


card_example = [('A', 'Spades'), ('K', 'Clubs'), (10, 'Diamonds'),
                (5, 'Hearts')]
deck = Deck(card_example)
deck.shuffle(card_example)
deck.take_cards(('A', 'Spades'), card_example)
