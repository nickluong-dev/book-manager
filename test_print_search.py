from unittest import TestCase
from books import print_search
from unittest.mock import patch
import io


class TestPrintSearch(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_first_book_one_result(self, mock_output):
        book = {'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}
        result = [{'Author': 'Nick Luong', 'Title': 'How to Not Code 101',
                                     'Publisher': 'Janky Coders 2020'}]
        print_search(book, result)
        expected = "1	Author: Nick Luong\n" \
                   "\tTitle: How to Not Code 101\n" \
                   "\tPublisher: Janky Coders 2020\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_first_book_two_results(self, mock_output):
        book = {'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}
        result = [{'Author': 'Nick Luong', 'Title': 'How to Not Code 101',
                   'Publisher': 'Janky Coders 2020'},
                  {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                   'Category': 'Architecture', 'Subject': 'American Architecture'}]
        print_search(book, result)
        expected = "1	Author: Nick Luong\n" \
                   "\tTitle: How to Not Code 101\n" \
                   "\tPublisher: Janky Coders 2020\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_real_second_book_two_results(self, mock_output):
        book = {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                     'Category': 'Architecture', 'Subject': '20th Century'}
        result = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                   'Category': 'Architecture', 'Subject': 'American Architecture'},
                  {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                   'Category': 'Architecture', 'Subject': '20th Century'}
                  ]
        print_search(book, result)
        expected = "2	Author: Dupre\n" \
                   "\tTitle: Skyscrapers\n" \
                   "\tPublisher: BD&L\n" \
                   "\tShelf: 12\n" \
                   "\tCategory: Architecture\n" \
                   "\tSubject: 20th Century\n\n"
        self.assertEqual(expected, mock_output.getvalue())

