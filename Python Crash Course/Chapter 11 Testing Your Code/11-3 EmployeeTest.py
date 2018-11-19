import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee('Jackson', 'Huang', 100000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertIn(self.employee, 105000)

    def test_give_custom_raise(self):
        self.employee.give_raise(100000)
        self.asserIn(self.employee, 200000)
