
from collections import namedtuple

class Card:
	"""Represents a playing card."""

	__slots__ = ["_suit", "_rank_name", "_rank_value"]

	def __init__(self, suit, rank_name, rank_value):
		self._suit = suit
		self._rank_name = rank_name
		self._rank_value = rank_value

	@property
	def rank_value(self):
		return self._rank_value

	def __repr__(self):
		return f"{self._rank_name} of {self._suit}"

	def adjusted_rank_value(self, aces_high=False):
		"""
		Method to return the rank of the card adjusted as needed if ace is high.
		"""
		return 14 if aces_high and self._rank_name == "Ace" \
			else self._rank_value

	# static methods
	@staticmethod
	def max(*args, aces_high=False):
		"""
		Static method to compare two or more cards and return the one with the highest rank.
		"""
		return max(
			args,
			key = lambda card: card.adjusted_rank_value(aces_high = aces_high)
		)

Rank = namedtuple("Rank", "name value")

class Deck:
	"""Represents a deck of cards."""

	__slots__ = ["_cards"]

	_SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
	_RANKS = (
		Rank(name="Ace", value=1),
		Rank(name="Two", value=2),
		Rank(name="Three", value=3),
		Rank(name="Four", value=4),
		Rank(name="Five", value=5),
		Rank(name="Six", value=6),
		Rank(name="Seven", value=7),
		Rank(name="Eight", value=8),
		Rank(name="Nine", value=9),
		Rank(name="Ten", value=10),
		Rank(name="Jack", value=11),
		Rank(name="Queen", value=12),
		Rank(name="King", value=13),
	)

	def __init__(self):
		self._cards = [ Card(suit, rank.name, rank.value)
						for suit in self._SUITS
						for rank in self._RANKS
		]

	@classmethod
	def stripped_deck(cls, *args):
		"""
		Class method to create a deck with the specified cards removed.
		"""
		deck = cls()
		deck._cards = [ card for card in deck._cards if card.rank_value not in args ]
		return deck

	@classmethod
	def piquet_deck(cls):
		"""
		Class method to create a piquet deck.
		"""
		return cls.stripped_deck(2, 3, 4, 5, 6)

	@property
	def cards(self):
		return self._cards


# deck = Deck()
# print(deck.cards)

deck2 = Deck.stripped_deck(2, 3, 4, 5, 6)
print(deck2.cards)

deck3 = Deck.piquet_deck()
print(deck3.cards)
