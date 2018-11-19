import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_names(self):
        formatted_name = get_formatted_name('Jackson', 'Huang')
        self.assertEqual(formatted_name, 'Jackson Huang')

    def test_first_middle_last_names(self):
        formatted_name = get_formatted_name('Jackson', 'Huang', 'Chang')
        self.assertEqual(formatted_name, 'Jackson Chang Huang')


unittest.main()
