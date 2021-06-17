import unittest

from game import playGame




class TestWon(unittest.TestCase):
    def test_won(self):
        won_game = False

        while won_game == False:
            won_game = playGame("Rock")
            print(won_game)

        self.assertTrue(won_game)

        won_game = False

        while won_game == False:
            won_game = playGame("Paper")
            print(won_game)

        self.assertTrue(won_game)
        
        won_game = False

        while won_game == False:
            won_game = playGame("Scissors")
            print(won_game)

        self.assertTrue(won_game)



if __name__ == '__main__':
    unittest.main()
