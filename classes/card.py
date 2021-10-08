from classes.utils.values import COLOURS_REPR, RANKS_REPR, COLOURS_NAMES, RANKS_NAMES, ACTIVITY


class Card:

    def __init__(self, rank, colour):
        assert 1 < rank < 15

        assert 0 < colour < 5

        self.rank = rank
        self.colour = colour

    def __repr__(self):
        return f"[{RANKS_REPR[self.rank]}{COLOURS_REPR[self.colour]}]"

    @property
    def name(self):
        return f"[{RANKS_NAMES[self.rank]} of {COLOURS_NAMES[self.colour]}s]"

    def __eq__(self, other):
        if self.rank == other.rank or self.colour == other.colour:
            return True

        return False

    def __bool__(self):
        return True


if __name__ == '__main__':
    card1 = Card(5, 1)
    card2 = Card(5, 2)
    card3 = Card(6, 2)

    print(card1.name)
    print(card2 == card3)
