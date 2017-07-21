import unittest
from app.conversion import conversion_to_num


class APITestCase(unittest.TestCase):

    def test_conversion_to_num_only_add(self):
        num = conversion_to_num("MMVI")
        self.assertTrue(num == 2006)

    def test_conversion_to_num_subtract(self):
        num = conversion_to_num("MCMXLIV")
        self.assertTrue(num == 1944)

    def test_conversion_to_num_succession_error(self):
        num = conversion_to_num("MMMM")
        self.assertTrue(num == 0)

    def test_conversion_to_num_roman_order_error(self):
        num = conversion_to_num("ID")
        self.assertTrue(num == 0)

        num = conversion_to_num("XD")
        self.assertTrue(num == 0)

        num = conversion_to_num("VX")
        self.assertTrue(num == 0)
