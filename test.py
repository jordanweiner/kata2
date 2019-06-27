import unittest
from stringcalc import add

class TestWeek1(unittest.TestCase):
	def test_empty_string(self):
		self.assertEqual(add(""), 0)

	def test_one_number_string(self):
		self.assertEqual(add("1"), 1)

	def test_two_number_string(self):
		self.assertEqual(add("12"), 3)

	def test_unknown_amount_of_numbers_string(self):
		self.assertEqual(add("123456"), 21)
		self.assertEqual(add("5293"), 19)

	def test_new_lines_btwn_numbers(self):
		self.assertEqual(add("123\n4"), 10)
		self.assertEqual(add("\n1234"), 10)
		self.assertEqual(add("1234\n"), 10)

	def test_commas_btwn_numbers(self):
		self.assertEqual(add("123,4"), 10)
		self.assertEqual(add(",1234"), 10)
		self.assertEqual(add("1234,"), 10)

	def test_new_lines__and_commas_btwn_numbers(self):
		self.assertEqual(add("1,23\n4"), 10)
		self.assertEqual(add("\n1234,"), 10)
		self.assertEqual(add(",1234\n"), 10)

if __name__ == '__main__':
    unittest.main()
