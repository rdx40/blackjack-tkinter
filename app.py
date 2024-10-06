import tkinter as tk
import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_aces()

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.message_label = tk.Label(root, textvariable=self.message, font=("Helvetica", 14))
        self.message_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.player_hit)
        self.hit_button.pack(pady=10)

        self.stand_button = tk.Button(root, text="Stand", command=self.player_stand)
        self.stand_button.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)


    def setup_game(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()

        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        self.update_display()

    def update_display(self):
        player_cards = ', '.join(str(card) for card in self.player_hand.cards)
        dealer_cards = ', '.join(str(card) for card in self.dealer_hand.cards[:1]) + " + [Hidden]"
        self.message.set(f"Player's Hand: {player_cards} (Value: {self.player_hand.value})\n"
                         f"Dealer's Hand: {dealer_cards}")

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal_card())
        if self.player_hand.value > 21:
            self.message.set(f"Bust! You lose. Your hand: {self.player_hand.value}")
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)
        else:
            self.update_display()

    def player_stand(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

        self.final_result()

    def final_result(self):
        player_value = self.player_hand.value
        dealer_value = self.dealer_hand.value

        dealer_cards = ', '.join(str(card) for card in self.dealer_hand.cards)
        self.message.set(f"Player's Hand: {player_value}\nDealer's Hand: {dealer_cards} (Value: {dealer_value})")

        if dealer_value > 21 or player_value > dealer_value:
            self.message.set(f"You win! Your hand: {player_value} Dealer hand: {dealer_value}")
        elif player_value < dealer_value:
            self.message.set(f"You lose! Your hand: {player_value} Dealer hand: {dealer_value}")
        else:
            self.message.set(f"It's a tie! Your hand: {player_value} Dealer hand: {dealer_value}")

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

    def restart_game(self):
        self.setup_game()
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()

