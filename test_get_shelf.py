from unittest import TestCase
from unittest.mock import patch
from books import get_shelf


class TestGetShelf(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_shelf_one(self, mock_input):
        expected = '1'
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['15'])
    def test_get_shelf_fifteen(self, mock_input):
        expected = '15'
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['island'])
    def test_get_shelf_island(self, mock_input):
        expected = 'island'
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['noguchi'])
    def test_get_shelf_island(self, mock_input):
        expected = 'noguchi'
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['99'])
    def test_get_shelf_invalid(self, mock_input):
        expected = None
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['0'])
    def test_get_shelf_invalid_two(self, mock_input):
        expected = None
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['asdf'])
    def test_get_shelf_invalid_three(self, mock_input):
        expected = None
        actual = get_shelf()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[''])
    def test_get_shelf_invalid_empty(self, mock_input):
        expected = None
        actual = get_shelf()
        self.assertEqual(actual, expected)
