from carddeck import CardDeck
from players import Players

# Creating an instance of the CardDeck class and two Player instance,
# where one is a dealer and the other is a regular player.
cd = CardDeck()
player = Players("Player")
dealer = Players("Dealer")

def game_loop():
    # The game loop runs the course of the game. First initalize the card deck,
    # then deals two cards to each in the sequence P, D, P, D. 
    init_cd = cd.init_card_deck()
    while len(player.hand) < 2 and len(dealer.hand) < 2:
        player.hand.append(init_cd.pop(0))
        dealer.hand.append(init_cd.pop(0))  

    while True:
    # This loop contains all the if statements that decide what the player
    # and dealer is to do in every situation and who wins.
        if player.calc_scores() == 21:
            print('Player wins!')
            print(player.show_hand())
            print(dealer.show_hand())
            break 
        
        if dealer.calc_scores() == 21: 
            print('Dealer wins!')
            print(player.show_hand())
            print(dealer.show_hand())
            break

        if player.calc_scores() == 22: 
            print('Dealer wins!')
            print(player.show_hand())
            print(dealer.show_hand())
            break
            
        if player.calc_scores() < 17:
            player.hand.append(init_cd.pop(0))
            if player.calc_scores() == 21:
                print('Player wins!') 
                print(player.show_hand()) 
                print(dealer.show_hand()) 
                break
            if player.calc_scores() > 21:
                print('Dealer wins!') 
                print(player.show_hand())
                print(dealer.show_hand())
                break
        
        if player.calc_scores() in [17,18,19,20] and player.calc_scores() > dealer.calc_scores():
            dealer.hand.append(init_cd.pop(0))
            if dealer.calc_scores() > player.calc_scores() and dealer.calc_scores() < 22:
                print('Dealer wins!') 
                print(player.show_hand())
                print(dealer.show_hand())
                break 
            if dealer.calc_scores() > player.calc_scores() and dealer.calc_scores() > 22:
                print('Player wins!') 
                print(player.show_hand())
                print(dealer.show_hand()) 
                break 
        else:
            print('Dealer wins!') 
            print(player.show_hand())
            print(dealer.show_hand())
            break 

if __name__ == '__main__':
    game_loop()

