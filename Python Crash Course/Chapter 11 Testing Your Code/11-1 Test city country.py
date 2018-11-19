import unittest
from city import city_function


class NamesCityTest(unittest.TestCase):

    def test_city_country(self):
        test = city_function('Santiago', 'Chile')
        self.assertEqual(test, 'Santiago, Chile')

    def test_city_country_population(self):
        test = city_function('Santiago', 'Chile', 5000000)
        self.assertEqual(test, 'Santiago, Chile - population 5000000')


unittest.main()
