class Players:
    # Player class makes the player and dealer able to have a hand of cards,
    # calculate their points and to show the hand at the end of a game. 
    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name

    def calc_scores(self):
        # Calculates the score and returnes it.
        return sum(x[-1] for x in self.hand)

    def show_hand(self):
        # Formats the cards and name of the players correctly 
        # into a string and then returns it.
        cards = [x[0] for x in self.hand]
        cards = ', '.join(cards)
        txt = "{}: {}"
        return txt.format(self.player_name, cards)
        
