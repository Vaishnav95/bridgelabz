"""Sorting Deck of Cards
@Purpose: Sorting the cards obtained by each player and arranging it in queue
@author: Vaishnav Goregaonkar
@date: 28/12/2019
"""

import random
from itertools import product
import queue_linked_list

# Suit of cards
glob_suit = ("Clubs", "Diamonds", "Hearts", "Spades")
# Rank of cards
glob_rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")


class Player:
    global glob_rank

    def __init__(self, data):
        self.deck_of_cards = data
        self.sort_cards()
        self.maintain_cards()
        self.print_deck()

    def sort_cards(self):
        """This method sorts the deck using bubble sort
        :return: sorted deck
        """
        for j in range(0, (len(self.deck_of_cards))):
            for i in range(0, (len(self.deck_of_cards) - j - 1)):
                pos = self.deck_of_cards[i]
                adj_pos = self.deck_of_cards[i + 1]
                if glob_rank.index(pos[1]) < glob_rank.index(adj_pos[1]):
                    temp = self.deck_of_cards[i]
                    self.deck_of_cards[i] = self.deck_of_cards[i + 1]
                    self.deck_of_cards[i + 1] = temp

    def maintain_cards(self):
        """This method maintains the deck of cards in a queue
        """
        self.sort_cards()
        cards_in_hand = queue_linked_list.Queue()
        for i in range(0, len(self.deck_of_cards)):
            cards_in_hand.en_queue(i)

    def print_deck(self):
        """This method prints the deck of cards maintained in the queue
        :return: displays the sorted deck
        """
        hand = queue_linked_list.Queue()
        for q in self.deck_of_cards:
            hand.en_queue(q)
        hand.print_list()


def deck_of_card():
    """This function produces a deck of cards from the given rank and suit"""

    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    cartesian_product = product(suit, rank)  # Using cartesian product to create deck
    list_cards = list(cartesian_product)
    random.shuffle(list_cards)  # Shuffling the cards
    distribute_card(list_cards)  # Distributing the cards
    return


def distribute_card(list_cards):
    """THis method distributes the cards among 4 players each having 9 cards"""
    # distributed_cards = []
    players = []
    counter = 0
    for j in range(4):
        new_list = []
        for k in range(9):
            new_list.append(list_cards[counter])
            counter += 1
        players.append(new_list)
    print_card(players)
    return


def print_card(player_cards):
    """This method displays the distributed cards"""
    players = queue_linked_list.Queue()
    for i in range(4):
        print("\nCards of player {} is :".format(i + 1))
        player = Player(player_cards[i])
        players.en_queue(player)
        players.print_list()


def main():
    deck_of_card()


# Driver Function
if __name__ == "__main__":
    main()
