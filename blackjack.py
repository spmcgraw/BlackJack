# Import needed libraries
import random
import datetime
from sys import exit

# Constants and Global Variables
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
rankValues = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, 
    "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

playing = True

# 1. Create Card

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# 2. Create Deck and include a shuffle

class Deck:

    def __init__(self):  # step through suits and ranks to create Card and Deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        singleCard = self.deck.pop
        return singleCard

# 3. Create Hand

class Hand:

    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += rankValues[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# 4. Create Player Profile with name, wallet, and hand
class Player:

    def __init__(self, name, wallet = 100):
        self.name = name
        self.wallet = wallet
        self.bet = 0
        self.hand = Hand()

    def print_hand(self): # Prints player's hand
        print("{}'s hand is: ".format(self.name))
        for card in self.hand.cards_in_hand:
            print(card.card_name)
            
# 5. Greet Player and ask for name
# 6. Ask player to bet, add to pot, and substract from player wallet
# 7. Deal to player and comp (hide comp until player stands)
# 8. Ask player to hit or stand
# 9. Annouce winner - If player wins add pot to their wallet
# 10. Ask player if they want to play again
