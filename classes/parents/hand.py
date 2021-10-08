from operator import attrgetter

from classes.card import Card


class Hand:
    def __init__(self):
        self._hand = []

    def add_card(self, card: Card):
        self._hand.append(card)

    def play_card(self, index=-1):
        if self._hand:
            return self._hand.pop(index)

    def __repr__(self):
        return f"[{' '.join(f'{i + 1}. {card}' for i, card in enumerate(self._hand))}]"

    def sort_by_colour(self):
        self._hand.sort(key=attrgetter('colour', 'rank'))

    def sort_by_rank(self):
        self._hand.sort(key=attrgetter('rank', 'colour'))

    def __len__(self):
        return len(self._hand)

    def __bool__(self):
        return bool(self._hand)