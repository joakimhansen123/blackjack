# blackjack
This is the submission of a solution for the technical task given as a part of the interview process.

The task chosen was number 2, blackjack and is written in Python v3.8.2. 

The program runs the card game blackjack between a player and the dealer. And then prints out who wins and both's cards.

The carddeck is first initialized, then players created, then two cards are dealt. The program then checks if the player or the dealer wins immediately. 
If they dont, the player draws cards until the player has more than 16 points. If the player does not get 21 or more than 21, the dealer draws card until
the dealer has more points than the player. If anyone at any point gets 21 they win and if they get more than 21 they lose immediately. When someone 
loses, the result and the players' cards are printed in the terminal.

Run main.py with the carddeck.py and players.py in the same directory.

Packages used: unittest and random.   
