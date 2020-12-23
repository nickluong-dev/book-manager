from unittest import TestCase
from unittest.mock import patch
from books import ask_search
import io


class TestAskSearch(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', 'abram'])
    def test_ask_search_valid_one(self, mock_input, mock_stdout):
        info = ({'Author': 'Abram', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        expected = ['Author', 'abram']
        expected_two = 'How do you want to search for the book?\n'
        actual = ask_search(info)
        self.assertEqual(actual, expected)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', 'computer'])
    def test_ask_search_valid_two(self, mock_input, mock_stdout):
        info = ({'Author': 'Abram', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': '', 'Title': 'Computer Stuff', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        expected = ['Title', 'computer']
        expected_two = 'How do you want to search for the book?\n'
        actual = ask_search(info)
        self.assertEqual(actual, expected)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', 'cOmpUter'])
    def test_ask_search_mixed_capitalization(self, mock_input, mock_stdout):
        info = ({'Author': 'Computer Made', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': '', 'Title': 'Computer Stuff', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        expected = ['Author', 'computer']
        expected_two = 'How do you want to search for the book?\n'
        actual = ask_search(info)
        self.assertEqual(actual, expected)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', 'asdf'])
    def test_ask_search_method_string(self, mock_input, mock_stdout):
        info = ({'Author': 'Computer Made', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': '', 'Title': 'Computer Stuff2', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        actual = ask_search(info)
        expected = ['Author', 'asdf']
        expected_two = 'How do you want to search for the book?\n'
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Chicken'])
    def test_ask_search_invalid_search_method_string_two(self, mock_input, mock_stdout):
        info = ({'Author': '', 'Title': 'Computer Stuff2', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': '', 'Title': 'Computer Stuff2', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        actual = ask_search(info)
        expected = None
        expected_two = 'How do you want to search for the book?\n'
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['100'])
    def test_ask_search_invalid_search_method_number(self, mock_input, mock_stdout):
        info = ({'Author': '', 'Title': 'Computer Stuff2', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                {'Author': 'Computer Made', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''})
        actual = ask_search(info)
        expected = None
        expected_two = 'How do you want to search for the book?\n'
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_two)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_ask_search_invalid_method_empty(self, mock_input, mock_stdout):
        info = ({'Author': 'hello', 'Title': 'asd', 'Publisher': 'fda', 'Shelf': 'f', 'Category': 'ds', 'Subject': 'f'},
                {'Author': 'df', 'Title': 'fa', 'Publisher': '432', 'Shelf': 'fd', 'Category': 'asdf', 'Subject': '22'})
        actual = ask_search(info)
        expected = None
        expected_two = 'How do you want to search for the book?\n'
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_two)
