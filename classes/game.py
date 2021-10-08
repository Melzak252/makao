from itertools import cycle

from classes.player import Player
from classes.utils.values import ACTIVITY
from deck import Deck


class Game:
    def __init__(self):
        self._players = []
        self._deck = Deck()
        self._discard_pile = Deck()
        self._player_cycle = None
        self.started = False
        self.top_card = None

    def __repr__(self):
        return "Game[\n" + "\n".join(repr(player) for player in self._players) + "\n]"

    def _start(self, no_decks):
        assert not self.started

        self.started = True

        self._player_cycle = cycle(self._players)

        for _ in range(no_decks):
            self._deck.add_deck()

        self._deck.shuffle()

        for player in self._player_cycle:
            if len(player) > 4:
                break

            player.add_card(self._deck.play_card())

        self.top_card = self._deck.play_card()

        while ACTIVITY[self.top_card.rank]:
            self._discard_pile.add_card(self.top_card)
            self.top_card = self._deck.play_card()

    def play(self, no_decks: int = 1):
        self._start(no_decks)

        for player in self._player_cycle:
            if not player.frozen:
                end = self._turn(player)

                if end:
                    break
            else:
                player.skip()

    def add_player(self, name: str = ""):
        if len(self._players) > 4:
            print("To many players!")
            return None

        self._players.append(Player(name))

    def kick_player(self, name):
        for i, player in enumerate(self._players):
            if player.name.lower() == name.lower():
                self._players.pop(i)
                return None

        print("There is no such player!")

    def _turn(self, player):
        player.sort_by_rank()
        print(f"Top card: {self.top_card}")
        print(player.name.title())
        print(player.turn)

        drawn_card = False
        indexes = None

        while indexes is None:
            drawn_card = False
            indexes = player.bot(self.top_card)

            try:
                indexes = [int(i) - 1 for i in indexes.split(" ")]
            except ValueError:
                print("Please insert indexes of your cards max 4 cards")
                indexes = None
                continue

            if -1 in indexes:
                drawn_card = True
                self.draw_cards(player, 1)
                break

            cards, indexes = self.process_indexes(indexes, player)

        if not drawn_card:
            self._discard_pile.add_card(self.top_card)
            self.top_card = cards[-1]
            self._discard_pile.extend(cards[:-1])
            if not len(player):
                print(f"{player.name.title()} Won!")
                return True

    def fill_deck(self):
        if len(self._discard_pile):
            self._deck.extend(self._discard_pile.drop_cards())
        else:
            print("Not enough cards to draw\nAdded new deck to pile")
            self._deck.add_deck()

        self._deck.shuffle()

    def process_indexes(self, indexes, player):
        cards = player.play_cards(indexes)

        if cards is None:
            return None, None

        if not cards[0] == self.top_card:
            print("First given card is not matching with top card")
            for card in cards:
                player.add_card(card)
            player.sort_by_rank()
            print(player.turn)
            return None, None

        return cards, indexes

    def draw_cards(self, player, no_cards):
        for _ in range(no_cards):
            if not (drawn_card := self._deck.play_card()):
                self.fill_deck()
                drawn_card = self._deck.play_card()
            player.add_card(drawn_card)


if __name__ == '__main__':
    game = Game()
    game.add_player("Melzak")
    game.add_player("Mazzy")
    game.add_player("Szymon")
    game.play()
    print()
    print(game)