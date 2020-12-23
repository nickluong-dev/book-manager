from unittest import TestCase
from books import get_search_methods


class TestGetSearch(TestCase):
    def test_get_search_methods_made_up(self):
        option = {'1': 'Element', '2': 'Class', '3': 'Race', '4': 'Weapon'}
        actual = get_search_methods(option)
        expected = "1. Type '1' to search by Element\n2. Type '2' to search by Class\n3. Type '3' to search by " \
                   "Race\n4. Type '4' to search by Weapon\n"
        self.assertEqual(expected, actual)

    def test_get_search_methods_real(self):
        option = {'1': 'Author', '2': 'Title', '3': 'Publisher'}
        actual = get_search_methods(option)
        expected = "1. Type '1' to search by Author\n2. Type '2' to search by Title\n3. " \
                   "Type '3' to search by Publisher\n"
        self.assertEqual(expected, actual)

    def test_get_search_methods_single(self):
        option = {'1': 'Author'}
        actual = get_search_methods(option)
        expected = "1. Type '1' to search by Author\n"
        self.assertEqual(expected, actual)

    def test_get_search_methods_empty(self):
        option = {}
        actual = get_search_methods(option)
        expected = ""
        self.assertEqual(expected, actual)
