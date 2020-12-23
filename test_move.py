from unittest import TestCase
from unittest.mock import patch
from books import move
import io


class TestMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_only_book_to_island(self, mock_output):
        test_results = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                         'Category': 'Architecture', 'Subject': 'American Architecture'}]
        test_move_parameters = [1, 'Island']
        move(test_results, test_move_parameters)
        expected = "You successfully moved 'Unbuilding' by 'Macaulay' to shelf: 'Island'\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_second_book_to_two(self, mock_output):
        test_results = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '5',
                         'Category': 'Architecture', 'Subject': 'American Architecture'},
                        {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                         'Category': 'Architecture', 'Subject': '20th Century'}]
        test_move_parameters = [2, '2']
        move(test_results, test_move_parameters)
        expected = "You successfully moved 'Skyscrapers' by 'Dupre' to shelf: '2'\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_last_book_to_thirty_five(self, mock_output):
        test_results = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '5',
                         'Category': 'Architecture', 'Subject': 'American Architecture'},
                        {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                         'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                         'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century',
                         'Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli',
                         'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}]
        test_move_parameters = [5, '35']
        move(test_results, test_move_parameters)
        expected = "You successfully moved 'Architecture 1979-1985' by 'Johnson Burgee' to shelf: '35'\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_middle_book_to_reading(self, mock_output):
        test_results = [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                         'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                         'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century',
                         'Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli',
                         'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'},
                        {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '5',
                         'Category': 'Architecture', 'Subject': 'American Architecture'}
                        ]
        test_move_parameters = [3, 'Reading']
        move(test_results, test_move_parameters)
        expected = "You successfully moved 'Architecture of the 20th Century' by 'Hollingsworth' to shelf: " \
                   "'Reading'\n\n"
        self.assertEqual(expected, mock_output.getvalue())
