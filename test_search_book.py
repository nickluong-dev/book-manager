from unittest import TestCase
from books import search_book


class TestSearchBook(TestCase):
    def test_search_book_return_one_search_title(self):
        collection = ({'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                     'Category': 'Architecture', 'Subject': 'American Architecture'},
                      {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                       'Publisher': ' Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'})
        actual = search_book(['Title', 'unbuilding'], collection)
        expected = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                     'Category': 'Architecture', 'Subject': 'American Architecture'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_several_title(self):
        collection = ({'Author': 'Leguin', 'Title': 'The Language of the Night Essays on Fantasy and Science Fiction',
                     'Publisher': 'Berkley Science Fiction', 'Shelf': '15', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                       'Publisher': 'Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'},
                      {'Author': 'Mendlesohn', 'Title': 'Rhetorics of Fantasy', 'Publisher': 'Wesleyan', 'Shelf': '36',
                       'Category': 'Literature', 'Subject': 'Criticism'},
                      {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                       'Category': 'Architecture', 'Subject': 'American Architecture'},
                      {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                       'Publisher': ' Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'})
        actual = search_book(['Title', 'fantasy'], collection)
        expected = [{'Author': 'Leguin', 'Title': 'The Language of the Night Essays on Fantasy and Science Fiction',
                     'Publisher': 'Berkley Science Fiction', 'Shelf': '15', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-', 'Publisher':
                        'Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'},
                    {'Author': 'Mendlesohn', 'Title': 'Rhetorics of Fantasy', 'Publisher': 'Wesleyan', 'Shelf': '36',
                     'Category': 'Literature', 'Subject': 'Criticism'},
                    {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                     'Publisher': ' Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_subject(self):
        collection = ({'Author': 'Leguin', 'Title': 'The Language of the Night Essays on Fantasy and Science Fiction',
                       'Publisher': 'Berkley Science Fiction', 'Shelf': '15', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                       'Publisher':'Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'},
                      {'Author': 'Mendlesohn', 'Title': 'Rhetorics of Fantasy', 'Publisher': 'Wesleyan', 'Shelf': '36',
                       'Category': 'Literature', 'Subject': 'Criticism'},
                      {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-',
                       'Publisher': ' Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'},
                      {'Author': 'Draper', 'Title': 'Stitch and Structure Design and Technique in 2- and 3-D textiles',
                       'Publisher': 'Batsford', 'Shelf': '34', 'Category': 'Art', 'Subject': 'Textiles'},
                      {'Author': 'Small', 'Title': 'Layered Cloth The Art of Fabric Manipulation', 'Publisher':
                          'Search Press', 'Shelf': '34', 'Category': 'Art', 'Subject': 'Textiles'},
                      {'Author': 'Wellesley-Smith', 'Title': 'Slow stitch mindful and contemplative textile art',
                       'Publisher': 'Batsford', 'Shelf': '6', 'Category': 'Art', 'Subject': 'Textiles'},
                      {'Author': 'Brackmann', 'Title': "The Surface Designer's Handbook", 'Publisher': 'None',
                       'Shelf': '34', 'Category': 'Technology', 'Subject': 'Textiles'},
                      {'Author': 'Gordon', 'Title': 'Textiles the Whole Story',
                       'Publisher': 'None', 'Shelf': '35', 'Category': 'Technology', 'Subject': 'Textiles'})
        actual = search_book(['Subject', 'textiles'], collection)
        expected = [{'Author': 'Draper', 'Title': 'Stitch and Structure Design and Technique in 2- and 3-D textiles',
                     'Publisher': 'Batsford', 'Shelf': '34', 'Category': 'Art', 'Subject': 'Textiles'},
                    {'Author': 'Small', 'Title': 'Layered Cloth The Art of Fabric Manipulation', 'Publisher':
                        'Search Press', 'Shelf': '34', 'Category': 'Art', 'Subject': 'Textiles'},
                    {'Author': 'Wellesley-Smith', 'Title': 'Slow stitch mindful and contemplative textile art',
                     'Publisher': 'Batsford', 'Shelf': '6', 'Category': 'Art', 'Subject': 'Textiles'},
                    {'Author': 'Brackmann', 'Title': "The Surface Designer's Handbook", 'Publisher': 'None',
                     'Shelf': '34', 'Category': 'Technology', 'Subject': 'Textiles'},
                    {'Author': 'Gordon', 'Title': 'Textiles the Whole Story',
                     'Publisher': 'None', 'Shelf': '35', 'Category': 'Technology', 'Subject': 'Textiles'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_publisher(self):
        collection = ({'Author': 'Larson and Pridmore', 'Title': 'Chicago Architecture and Design',
                       'Publisher': 'Abrams', 'Shelf': 'Noguchi', 'Category': 'Architecture',
                       'Subject': 'American Architecture'},
                      {'Author': 'Wiseman', 'Title': 'I. M. Pei A Profile in American Architecture',
                       'Publisher': 'Abrams', 'Shelf': 'Noguchi', 'Category': 'Architecture',
                       'Subject': 'American Architecture'},
                      {'Author': 'Polkonen (ed) et al', 'Title': 'Eero Saarinen Shaping the Future',
                       'Publisher': 'Yale University Press', 'Shelf': 'Noguchi', 'Category': 'Architecture',
                       'Subject': 'Architecture'},
                      {'Author': 'Crow', 'Title': 'Nancy Crow', 'Publisher': 'Breckling Press', 'Shelf': 'Noguchi',
                       'Category': 'Art', 'Subject': 'Quilting'})
        actual = search_book(['Publisher', 'abrams'], collection)
        expected = [{'Author': 'Larson and Pridmore', 'Title': 'Chicago Architecture and Design', 'Publisher': 'Abrams',
                     'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': 'American Architecture'},
                    {'Author': 'Wiseman', 'Title': 'I. M. Pei A Profile in American Architecture',
                     'Publisher': 'Abrams', 'Shelf': 'Noguchi', 'Category': 'Architecture',
                     'Subject': 'American Architecture'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_category(self):
        collection = ({'Author': 'Fung', 'Title': 'The Obesity Code', 'Publisher': 'Greystone', 'Shelf': 'Reading',
                       'Category': 'Health', 'Subject': 'Nutrition'},
                      {'Author': 'Gidwold and Morgan', 'Title': 'Basic Training  Fundamental Guide to Fitness for Men',
                       'Publisher': "St Martin's Press", 'Shelf': '19', 'Category': 'Health', 'Subject': 'Working out'},
                      {'Author': 'Hix', 'Title': 'Working Out The Shape-up Guide for Men',
                       'Publisher': 'Simon & Schuster', 'Shelf': '19', 'Category': 'Health', 'Subject': 'Working out'})
        actual = search_book(['Category', 'health'], collection)
        expected = [{'Author': 'Fung', 'Title': 'The Obesity Code', 'Publisher': 'Greystone', 'Shelf': 'Reading',
                     'Category': 'Health', 'Subject': 'Nutrition'},
                    {'Author': 'Gidwold and Morgan', 'Title': 'Basic Training  Fundamental Guide to Fitness for Men',
                     'Publisher': "St Martin's Press", 'Shelf': '19', 'Category': 'Health', 'Subject': 'Working out'},
                    {'Author': 'Hix', 'Title': 'Working Out The Shape-up Guide for Men',
                     'Publisher': 'Simon & Schuster', 'Shelf': '19', 'Category': 'Health', 'Subject': 'Working out'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_author_partial_search(self):
        collection = ({'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abramowitz', 'Title': 'Knishes & Know-how: Jewish cooking for everyone',
                       'Publisher': '"Holt, Rinehard and Winston of Canada"', 'Shelf': '9', 'Category': 'Food',
                       'Subject': 'Jewish'},
                      {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                       'Shelf': '2', 'Category': 'Language', 'Subject': 'English'})
        actual = search_book(['Author', 'abram'], collection)
        expected = [{'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abramowitz', 'Title': 'Knishes & Know-how: Jewish cooking for everyone',
                     'Publisher': '"Holt, Rinehard and Winston of Canada"', 'Shelf': '9', 'Category': 'Food',
                     'Subject': 'Jewish'},
                    {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                     'Shelf': '2', 'Category': 'Language', 'Subject': 'English'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_shelf(self):
        collection = ({'Author': 'Perdue', 'Title': "The Unofficial Lego Mindstorms NXT Inventor's Guide",
                       'Publisher': 'No Starch Press', 'Shelf': 'Lego', 'Category': 'Science', 'Subject': 'Robotics'},
                      {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                       'Shelf': '2', 'Category': 'Language', 'Subject': 'English'})
        actual = search_book(['Shelf', 'lego'], collection)
        expected = [{'Author': 'Perdue', 'Title': "The Unofficial Lego Mindstorms NXT Inventor's Guide",
                     'Publisher': 'No Starch Press', 'Shelf': 'Lego', 'Category': 'Science', 'Subject': 'Robotics'}]
        self.assertEqual(actual, expected)

    def test_search_book_return_random(self):
        collection = ({'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6',
                       'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                      {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                       'Shelf': '2', 'Category': 'Language', 'Subject': 'English'})
        actual = search_book(['Publisher', 'fdsasdf'], collection)
        expected = []
        self.assertEqual(actual, expected)
