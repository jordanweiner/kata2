import unittest
from stringcalc import add

class TestWeek1(unittest.TestCase):
	def test_sum_when_zero_numbers_in_string(self):
		self.assertEqual(add(""), 0)

	def test_sum_when_one_number_in_string(self):
		self.assertEqual(add("1"), 1)
		self.assertEqual(add("2"), 2)

	def test_sum_when_two_numbers_in_string(self):
		self.assertEqual(add("12"), 3)

if __name__ == '__main__':
    unittest.main()
