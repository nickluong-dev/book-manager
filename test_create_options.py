from unittest import TestCase
from books import create_options


class TestCreateOptions(TestCase):
    def test_create_test_headers(self):
        collection = ({'Material': '', 'Class': '', 'Ingredient': '', 'Price': '', 'Age': '', 'Food': ''},
                      {'Material': '1', 'Class': '1', 'Ingredient': '1', 'Price': '1', 'Age': '1', 'Food': '1'})
        actual = create_options(collection)
        expected = {'1': 'Material', '2': 'Class', '3': 'Ingredient', '4': 'Price', '5': 'Age', '6': 'Food'}
        self.assertEqual(actual, expected)

    def test_create_options_test_headers_two(self):
        collection = ({'Damage': '', 'Health': '', 'Resistance': '', 'Dexterity': '', 'Mana': '', 'Class': ''},
                      {'Damage': '1', 'Health': '1', 'Resistance': '1', 'Dexterity': '1', 'Mana': '1', 'Class': '1'})
        actual = create_options(collection)
        expected = {'1': 'Damage', '2': 'Health', '3': 'Resistance', '4': 'Dexterity', '5': 'Mana', '6': 'Class'}
        self.assertEqual(actual, expected)

    def test_create_options_real_headers(self):
        collection = ({'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', 'Subject': ''},
                      {'Author': '1', 'Title': '1', 'Publisher': '1', 'Shelf': '1', 'Category': '1', 'Subject': '1'})
        actual = create_options(collection)
        expected = {'1': 'Author', '2': 'Title', '3': 'Publisher', '4': 'Shelf', '5': 'Category', '6': 'Subject'}
        self.assertEqual(actual, expected)
