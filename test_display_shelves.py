from unittest import TestCase
from unittest.mock import patch
from books import display_shelves
import io


class TestDisplayShelves(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_shelves(self, mock_stdout):
        display_shelves()
        expected = "Shelves:\n" \
                   "1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|\n" \
                   "23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|Gaby|Island|Lego|Noguchi|Reading|Students|\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
