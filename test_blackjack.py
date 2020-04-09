import unittest
from carddeck import CardDeck
from players import Players

class TestBlackjack(unittest.TestCase):
    def test_init_card_deck(self):
        # Tests a pseudorandom set of cards are included in the carddeck
        # and that the carddeck contains 52 cards.
        cd = CardDeck()
        init_cd = cd.init_card_deck()

        self.assertIn(['D9', 9], init_cd)
        self.assertIn(['SJ', 10], init_cd)
        self.assertIn(['HA', 11], init_cd)
        self.assertNotIn(['Q2', 2], init_cd)
        self.assertEqual(len(init_cd), 52)

    def test_calc_scores(self):
        # Tests that the correct score is calculated.
        player = Players("Player")
        player.hand = [['H7', 7], ['DQ', 10]]

        self.assertEqual(player.calc_scores(), 17)

    def test_show_hand(self):
        # Tests that the string formating when showing the hand is correct. 
        player = Players("Player")
        player.hand = [['H1', 1], ['SA', 11]]
        
        self.assertEqual(player.show_hand(), "Player: ['H1', 'SA']")

        