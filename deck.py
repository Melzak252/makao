from random import shuffle
from typing import Iterable

from classes.card import Card
from classes.parents.hand import Hand


class Deck(Hand):

    def __init__(self):
        super().__init__()

    def extend(self, deck: Iterable[Card]):
        self._hand.extend(deck)

    def add_deck(self):
        for i in range(2, 15):
            for j in range(1, 5):
                self._hand.append(Card(i, j))

    def drop_cards(self):
        cards, self._hand = self._hand, list()
        return cards

    def shuffle(self):
        shuffle(self._hand)

    def __iter__(self):
        return self._hand

    def __getitem__(self, item):
        return self._hand[item]


if __name__ == '__main__':
    deck = Deck()
    deck.add_deck()
    deck.shuffle()
    print(deck)
