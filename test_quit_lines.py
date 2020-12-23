from unittest import TestCase
from books import quit_lines


class TestQuitLines(TestCase):

    def test_quit_lines_test_book(self):
        example_book = {'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}
        actual = quit_lines(example_book)
        expected = 'Nick Luong\tHow to Not Code 101\tJanky Coders 2020'
        self.assertEqual(actual, expected)

    def test_quit_lines_actual_book_one(self):
        example_book = {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                        'Category': 'Architecture', 'Subject': 'American Architecture'}
        actual = quit_lines(example_book)
        expected = 'Macaulay\tUnbuilding\tHMCo\t6\tArchitecture\tAmerican Architecture'
        self.assertEqual(actual, expected)

    def test_quit_lines_actual_book_two(self):
        example_book = {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century',
                        'Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}
        actual = quit_lines(example_book)
        expected = 'Hollingsworth\tArchitecture of the 20th Century\tExeter\t6\tArchitecture\t20th Century'
        self.assertEqual(actual, expected)



