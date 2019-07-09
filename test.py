import unittest
from stringcalc import add

class TestWeek1(unittest.TestCase):
	def test_empty_string(self):
		self.assertEqual(add(""), 0)

if __name__ == '__main__':
    unittest.main()
