from unittest import TestCase
from unittest.mock import patch
from books import menu
import io


class TestMenu(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_menu_move(self, mock_input):
        expected = '1'
        actual = menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_menu_search(self, mock_input):
        expected = '2'
        actual = menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_menu_quit(self, mock_input):
        expected = '3'
        actual = menu()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_invalid(self, mock_stdout, mock_input):
        menu()
        expected = "Welcome to your virtual book shelf. Please select an option. You can type in lowercase.\n" \
                   "That is not a valid option. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['asdfasdf !'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_random_string(self, mock_stdout, mock_input):
        menu()
        expected = "Welcome to your virtual book shelf. Please select an option. You can type in lowercase.\n" \
                   "That is not a valid option. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_random_string(self, mock_stdout, mock_input):
        menu()
        expected = "Welcome to your virtual book shelf. Please select an option. You can type in lowercase.\n" \
                   "That is not a valid option. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())



