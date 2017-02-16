import unittest
from unittest.mock import patch
import user_interface


class TestUI(unittest.TestCase):

    #TODO test the user interface better. Separate the UI better than what it is now
    @patch('builtins.input')
    def test_get_opponent(self, mock_input):
        # testing the user input for getting the opponent name
        mock_input.side_effect = ['packers']
        opponent = user_interface.get_opponent()
        self.assertEqual('packers', opponent)

    @patch('builtins.input')
    def test_get_location(self, mock_input):
        # testing the user input for getting the location
        mock_input.side_effect = ['green bay']
        location = user_interface.get_location()
        self.assertEqual('green bay', location)

    @patch('builtins.input')
    def test_get_date(self, mock_input):
        # testing the user input for getting the date
        mock_input.side_effect = ['12/13/14']
        date = user_interface.get_date()
        self.assertEqual('12/13/14', date)

if __name__ == '__main__':
    unittest.main()