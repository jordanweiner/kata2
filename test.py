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

	def test_sum_when_unknown_amount_of_numbers_in_string(self):
		self.assertEqual(add("1234"), 10)
		self.assertEqual(add("12345"), 15)

	def test_sum_when_newlines_btwn_numbers_in_string(self):
		self.assertEqual(add("1\n2\n3"), 6)
		self.assertEqual(add("1\n23"), 6)

	def test_sum_when_newlines_at_ends_of_numbers_in_string(self):
		self.assertEqual(add("\n123\n"), 6)

	def test_sum_when_commas_btwn_numbers_in_string(self):
		self.assertEqual(add("1,2,3"), 6)
		self.assertEqual(add("1,23"), 6)

	def test_sum_when_commas_at_ends_of_numbers_in_string(self):
		self.assertEqual(add(",123,"), 6)

	def test_sum_when_commas_and_newlines_in_string(self):
		self.assertEqual(add(",1\n2\n3,"), 6)

if __name__ == '__main__':
    unittest.main()
