from unittest import TestCase
from books import get_info


class TestGetInfo(TestCase):
    def test_get_info(self):
        file = 'Books_short_test.txt'
        expected = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12',
                     'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Hollingsworth','Title': 'Architecture of the 20th Century', 'Publisher': 'Exeter',
                     'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'},
                    {'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli',
                     'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'})
        actual = get_info(file)
        self.assertEqual(expected, actual)
