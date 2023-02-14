import unittest 
from unittest.mock import patch
from io import StringIO

from RPS import RPS_game

class TestUserInput(unittest.TestCase):

    @patch('sys.stdin', StringIO('R\nS'))
    def test_player1_R_win(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 1"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('R\nP'))
    def test_player1_R_lose(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 2"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('R\nR'))
    def test_player1_R_tie(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Tie"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('S\nP'))
    def test_player1_S_win(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 1"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('S\nR'))
    def test_player1_S_lose(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 2"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('S\nS'))
    def test_player1_S_tie(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Tie"

        #Check values
        self.assertEqual(x, expected)
    
    @patch('sys.stdin', StringIO('P\nR'))
    def test_player1_P_win(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 1"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('P\nS'))
    def test_player1_P_lose(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Player 2"

        #Check values
        self.assertEqual(x, expected)

    @patch('sys.stdin', StringIO('P\nP'))
    def test_player1_R_tie(self):
        #Run the function
        x = RPS_game()

        #Save what we are expecting
        expected= "Tie"

        #Check values
        self.assertEqual(x, expected)



    
if __name__ == '__main__':
    unittest.main()