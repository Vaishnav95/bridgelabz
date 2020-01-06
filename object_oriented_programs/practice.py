import random


class Deck:
    """This class contains deck of cards having suit and rank which can be shuffled and distributed
    """
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def pack_of_cards(self):
        """This method creates a deck of 52 cards

        :return: self.cards: a list of cards
        """
        for i in self.suit:
            for j in self.rank:
                self.cards.append(j + " of " + i)  # Appending the possible cards in the empty list
        return self.cards

    def players_shuffle(self):
        """This method shuffles the deck of cards for 4 players and distributing 9 cards to each player

        :return: prints the cards distributed to the four players
        """
        global shuffle_cards
        shuffle_cards = random.sample(self.pack_of_cards(), 36)  # 36 is the total cards needed(9*4)
        print(shuffle_cards)

        global first, second, third, fourth
        first = shuffle_cards[:9]
        second = shuffle_cards[9:18]
        third = shuffle_cards[18:27]
        fourth = shuffle_cards[27:]

        print("Player 1: ", first, "\nPlayer 2: ", second, "\nPlayer 3: ", third, "\nPlayer 4: ", fourth)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(Deck):
    def __init__(self, data):
        self.start_node = None

    def list_to_linked(self):
        assert len(shuffle_cards) > 0
        if len(shuffle_cards) == 1:
            return LinkedList(shuffle_cards[0])
        else:
            return LinkedList(shuffle_cards[0], LinkedList.list_to_linked(shuffle_cards[1:]))

    def f_display(self):
        current = self.start_node
        temp = ""
        while current:
            print(current.data, "-->", end=" ")
            current = current.ref
        return


if __name__ == '__main__':
    new = LinkedList(Deck)
    new.f_display()

