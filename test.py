import unittest

from game import playGame




class TestWon(unittest.TestCase):
    def test_won(self):
        won_game = False

        while won_game == False:
            won_game = playGame("Rock")
            

        self.assertTrue(won_game)

        won_game = False

        while won_game == False:
            won_game = playGame("Paper")
            

        self.assertTrue(won_game)

        won_game = False

        while won_game == False:
            won_game = playGame("Scissors")
            

        self.assertTrue(won_game)



if __name__ == '__main__':
    unittest.main()
