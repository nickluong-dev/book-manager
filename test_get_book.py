from unittest import TestCase
from unittest.mock import patch
from books import get_book


class TestGetBook(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_book_first(self, mock_input):
        results = [{'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6',
                    'Category': 'Architecture', 'Subject': '20th Century'},
                   {'Author': 'Beer and Johnston', 'Title': 'Vector Mechanics for Engineers Statics and Dynamics',
                    'Publisher': 'McGraw Hill', 'Shelf': '27', 'Category': 'Mathematics',
                    'Subject': 'Vector Mechanics'}]

        actual = get_book(results)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_get_book_middle(self, mock_input):
        results = [{'Author': 'Leguin', 'Title': 'The Language of the Night Essays on Fantasy and Science Fiction',
                    'Publisher': 'Berkley Science Fiction', 'Shelf': '15', 'Category': 'Fiction', 'Subject': 'SF'},
                   {'Author': 'Tucker', 'Title': 'FF Dot. -The Pixel Art of FINAL FANTASY-', 'Publisher':
                       'Square Enix Co', 'Shelf': '35', 'Category': 'Games', 'Subject': 'Graphics'},
                   {'Author': 'Mendlesohn', 'Title': 'Rhetorics of Fantasy', 'Publisher': 'Wesleyan', 'Shelf': '36',
                    'Category': 'Literature', 'Subject': 'Criticism'},
                   {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
                    'Category': 'Architecture', 'Subject': 'American Architecture'}]

        actual = get_book(results)
        expected = 3
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['15'])
    def test_get_book_last_item(self, mock_input):
        results = [{'Author': 'Barton', 'Title': 'Dungeons and Desktops the History of Computer Role-Playing Games',
                    'Publisher': 'A K Peters', 'Shelf': '4', 'Category': 'Games', 'Subject': 'History'},
                   {'Author': 'Knuth', 'Title': 'The Art of Computer Programming Volume 1 Fundamental Algorithms',
                    'Publisher': 'Addison Wesley', 'Shelf': '37', 'Category': 'Programming', 'Subject': 'Algorithms'},
                   {'Author': 'Knuth', 'Title': 'The Art of Computer Programming Volume 2 Seminumerical Algorithms',
                    'Publisher': 'Addison Wesley', 'Shelf': '37', 'Category': 'Programming', 'Subject': 'Algorithms'},
                   {'Author': 'Knuth', 'Title': 'The Art of Computer Programming Volume 3 Sorting and Searching',
                    'Publisher': 'Addison Wesley', 'Shelf': '37', 'Category': 'Programming', 'Subject': 'Algorithms'},
                   {'Author': 'Levy', 'Title': 'The Joy of Computer Chess', 'Publisher': 'Prentice Hall', 'Shelf': '3',
                    'Category': 'Programming', 'Subject': 'Artificial Intelligence'},
                   {'Author': 'Foley and Van Dam', 'Title': 'Fundamentals of Interactive Computer Graphics',
                    'Publisher': 'Addison Wesley', 'Shelf': '21', 'Category': 'Programming', 'Subject': 'Graphics'},
                   {'Author': 'Filho', 'Title': 'Computer Science Distilled', 'Publisher': 'Code Energy', 'Shelf': '22',
                    'Category': 'Science', 'Subject': 'Computational Thinking'},
                   {'Author': 'Christian', 'Title': 'Algorithms to Live By The Computer Science of Human Decisions',
                    'Publisher': 'Picador', 'Shelf': 'Reading', 'Category': 'Science', 'Subject': 'Computer science'},
                   {'Author': 'Givone and Roesser', 'Title': 'Microprocessor / Micrcomputers: An Introduction',
                    'Publisher': 'McGraw Hill', 'Shelf': 'Island', 'Category': 'Science',
                    'Subject': 'Computer science'},
                   {'Author': 'Mano', 'Title': 'Digital Logic and Computer Design', 'Publisher': 'Prentice Hall',
                    'Shelf': 'Island', 'Category': 'Science', 'Subject': 'Computer science'},
                   {'Author': 'Nisan and Schocken', 'Title': 'The Elements of Computer Systems',
                    'Publisher': 'MIT Press', 'Shelf': '21', 'Category': 'Science', 'Subject': 'Computer science'},
                   {'Author': 'Tanenbaum', 'Title': 'Computer Networks', 'Publisher': 'Prentice Hall',
                    'Shelf': 'Island', 'Category': 'Science', 'Subject': 'Computer science'},
                   {'Author': 'Tremblay and Bunt',
                    'Title': 'An Introduction to Computer Science an Algorithmic Approach',
                    'Publisher': 'McGraw Hill', 'Shelf': 'Island', 'Category': 'Science',
                    'Subject': 'Computer science'},
                   {'Author': "Bryant and O'Hallaron", 'Title': "Computer Systems A Programmer's Perspective 2e",
                    'Publisher': 'Prentice Hall', 'Shelf': '21', 'Category': 'Science', 'Subject': 'Computer systems'},
                   {'Author': 'Forsyth and Ponce', 'Title': 'Computer Vision a Modern Approach 2e',
                    'Publisher': 'Prentice Hall', 'Shelf': '21', 'Category': 'Science', 'Subject': 'Computer vision'},
                   {'Author': 'Wiltshire', 'Title': 'Home Computers: 100 Icons that Defined a Digital Generation',
                    'Publisher': 'MIT Press', 'Shelf': 'Reading', 'Category': 'Technology', 'Subject': 'History'}]
        actual = get_book(results)
        expected = 15
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['asdf'])
    def test_get_book_invalid_string(self, mock_input):
        results = [{'Author': 'Bagnall', 'Title': 'Maximum Lego EV3', 'Publisher': 'Variant Press', 'Shelf': 'Students',
                    'Category': 'Programming', 'Subject': 'Java'}]

        actual = get_book(results)
        expected = None
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['99'])
    def test_get_book_invalid_number(self, mock_input):
        results = [{'Author': 'Bagnall', 'Title': 'Maximum Lego EV3', 'Publisher': 'Variant Press', 'Shelf': 'Students',
                    'Category': 'Programming', 'Subject': 'Java'}]

        actual = get_book(results)
        expected = None
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[''])
    def test_get_book_empty(self, mock_input):
        results = [{'Author': 'Wiltshire', 'Title': 'Home Computers: 100 Icons that Defined a Digital Generation',
                    'Publisher': 'MIT Press', 'Shelf': 'Reading', 'Category': 'Technology', 'Subject': 'History'}]

        actual = get_book(results)
        expected = None
        self.assertEqual(actual, expected)

