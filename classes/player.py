from classes.parents.hand import Hand


class Player(Hand):
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
        self.frozen = 0

    def play_cards(self, indexes):

        if not len(indexes) in [1, 3, 4]:
            print("Incorrect number of cards")
            return None

        if any(index >= len(self._hand) or index < 0 for index in indexes):
            print("Index out of scope!")
            return None

        fitst_card = self._hand[indexes[0]]

        if any(fitst_card.rank != self._hand[i].rank for i in indexes):
            print("Cards have no the same rank")
            return None

        cards = []
        for i, index in enumerate(indexes):
            index -= sum(1 for j in indexes[:i] if j < index)
            cards.append(self._hand.pop(index))

        return cards

    def skip(self):
        self.frozen -= 1

    @property
    def turn(self):
        return "0. Draw a card\n" + "\n".join(f'{i + 1}. {card}' for i, card in enumerate(self._hand))

    def __repr__(self):
        return self.name.title() + super().__repr__()

    def bot(self, top_card):
        for i, card in enumerate(self._hand):
            if card == top_card:
                return f"{i + 1}"
        return "0"
