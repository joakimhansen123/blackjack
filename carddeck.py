import random

class CardDeck:
    # Provides a shuffled deck of 52 unique cards. 
    def __init__(self):
        self.card_deck = []
        self.card_name = "{}{}"

    def init_card_deck(self):
        # Adds one of each type of card to the deck and then shuffles it. 
        # Returns the carddeck.
        for i in ["C", "D", "H", "S"]:
            for j in range(2, 11):
                self.card_deck.append([self.card_name.format(i, j), j])
            for k in ["J", "Q", "K"]:
                self.card_deck.append([self.card_name.format(i, k), j])
            self.card_deck.append([self.card_name.format(i, "A"), 11])
        
        random.shuffle(self.card_deck)

        return self.card_deck 