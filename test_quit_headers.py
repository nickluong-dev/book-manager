from unittest import TestCase
from books import quit_headers


class TestQuitHeaders(TestCase):

    def test_quit_headers_books_file(self):
        expected = 'Author\tTitle\tPublisher\tShelf\tCategory\tSubject'
        actual = quit_headers(({'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '',
                                'Subject': ''},
                               {'Author': '1', 'Title': '1', 'Publisher': '1', 'Shelf': '1', 'Category': '1',
                                'Subject': '1'}))
        self.assertEqual(expected, actual)

    def test_quit_headers_different_test_file(self):
        expected = 'Damage\tHealth\tResistance\tDexterity\tMana\tClass'
        actual = quit_headers(({'Damage': '', 'Health': '', 'Resistance': '', 'Dexterity': '', 'Mana': '',
                                'Class': ''},
                               {'Damage': '1', 'Health': '1', 'Resistance': '1', 'Dexterity': '1', 'Mana': '1',
                                'Class': '1'}))
        self.assertEqual(expected, actual)
