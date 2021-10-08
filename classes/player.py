from classes.parents.hand import Hand


class Player(Hand):
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
        self.frozen = 0

    def play_cards(self, *ids):
        if not len(ids) in [1, 3, 4]:
            print("Incorrect number of cards")

        fitst_card = self._hand[ids[0]]
        if any(fitst_card.rank != self._hand[i].rank for i in ids):
            print("Cards have no the same rank")
            return None

        cards = []
        for i, index in enumerate(ids):
            index -= sum(1 for j in ids[:i] if j < index)
            cards.append(self._hand.pop(index))

        return cards

    def skip(self):
        self.frozen -= 1
