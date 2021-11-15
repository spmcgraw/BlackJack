"""Import needed libraries"""
import random
import datetime
from sys import exit

# Constants and Global Variables
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
        "Queen", "King", "Ace"]
rankValues = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
    "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

PLAYING = True

# 1. Create Card

class Card:
    """Build out the cards"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# 2. Create Deck and include a shuffle

class Deck:
    """Build out the deck using Card class"""
    def __init__(self):  # step through suits and ranks to create Card and Deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """shuffles the deck"""
        random.shuffle(self.deck)

    def deal(self):
        """Deals the cards one at a time"""
        single_card = self.deck.pop
        return single_card

# 3. Create Hand

class Hand:
    """Build out the hand"""
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """Adds up the value of the cards"""
        self.cards.append(card)
        self.value += rankValues[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_aces(self):
        """checks if a card is an ace and makes it a 1 if over 21"""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# 4. Create Player and Dearler Profiles with name, wallet, and hand
class Player:
    """Build out player profile"""
    def __init__(self, name, wallet = 100):
        self.name = name
        self.wallet = wallet
        self.bet = 0
        self.hand = Hand()

    def print_hand(self):
        """Prints player's hand"""
        print(f"{self.name}'s hand is: ")
        for card in self.hand.cards:
            print(card.card_name)

    def update_wallet(self, result, pot):
        """Updates the player's wallet if they won"""
        if result == "won":
            self.wallet += pot
        else:
            self.wallet -= pot

class Dealer:
    """Build out dealer profile"""
    def __init__(self):
        self.hand = Hand()

    # Print dealer hand in stages
    def print_hand_stage1(self):
        """Prints dealer's hand"""
        print("\nDealer's hand is: ")
        print("<card hidden>")
        print(f" {self.hand.cards[1]}")

    def print_hand_all(self):
        """Show's dealer's hand and value"""
        print("\nDealer's hand is: ", *self.hand.cards, sep="\n")
        print("Dealer's hand =", self.hand.value)

# 5. Greet Player and ask for name
# 6. Ask player to bet, add to pot, and substract from player wallet
# 7. Deal to player and comp (hide comp until player stands)
# 8. Ask player to hit or stand
# 9. Annouce winner - If player wins add pot to their wallet
# 10. Ask player if they want to play again
