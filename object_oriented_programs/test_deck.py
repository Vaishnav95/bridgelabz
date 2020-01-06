import pytest
from object_oriented_programs.deck import Deck

deck_test = Deck()


def test_pack():
    # deck_test.pack_of_cards()
    # deck_test.players_shuffle()
    assert len(deck_test.suit) == 4
    assert len(deck_test.rank) == 13


def test_shuffle():
    assert len(deck_test.players_shuffle()) == 36


def test_type():
    hasattr(deck_test.pack_of_cards(), "cards")
    hasattr(deck_test.players_shuffle(), "shuffle_cards")
    hasattr(deck_test.players_shuffle(), "first, second, third, fourth")


pytest.main()
