import unittest
import StringIO
import sys
from stringcalc import add

class TestWeek1(unittest.TestCase):
	def test_sum_when_zero_numbers_in_string(self):
		self.assertEqual(add(""), 0)

	def test_sum_when_one_number_in_string(self):
		self.assertEqual(add("1"), 1)
		self.assertEqual(add("2"), 2)

	def test_sum_when_two_numbers_in_string(self):
		self.assertEqual(add("12"), 3)

class TestWeek2(unittest.TestCase):
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

class TestWeek3(unittest.TestCase):
	def test_sum_when_delimiter_specified(self):
		self.assertEqual(add("//[;]\n1;2"), 3)

	def test_sum_when_delimeter_not_specified(self):
		self.assertEqual(add("1,23\n4"), 10)

	def test_exception_thrown_when_string_has_negative_number(self):
		self.assertRaises(Exception, add, "1-2;3")

	def test_error_message_when_exception_thrown_on_neg_number(self):
		with self.assertRaises(Exception) as error:
			add("//[;]\n1;-23")
		self.assertEqual(error.exception.message, 'negatives not allowed: -23')

	def test_sum_when_delimiter_specified_and_numbers_greater_than_9(self):
		self.assertEqual(add("//[;]\n1;20"), 21)

	def test_sum_when_string_has_numbers_over_1000(self):
		self.assertEqual(add("//[oo]\n1oo1000oo1001"), 1001)

class TestWeek4(unittest.TestCase):
	def test_sum_when_string_has_multiple_delimeters(self):
		self.assertEqual(add("//[*][%]\n1*2%3"), 6)

	def test_sum_when_string_has_multiple_delimeters_with_more_than_one_char(self):
		self.assertEqual(add("//[*&][%%%%][^]\n1*&2%%%%3^4"), 10)

	def test_sum_returned_to_console_when_given_string(self):
		output = StringIO.StringIO()
		sys.stdout = output
		add("//[*][%]\n1*2%3")
		sys.stdout = sys.__stdout__
		self.assertEqual(output.getvalue(), "\n6\n")

if __name__ == '__main__':
    unittest.main()
