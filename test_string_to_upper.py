import unittest
import string_to_upper as stu

class TestStringToUpper(unittest.TestCase):

	def setup(self):
		pass

	def test_first_case(self):
		case = "wyraz1    wyraz3"
		self.assertEqual(stu.string_to_upper(case),"Wyraz1    Wyraz3")

	def test_second_case(self):
		case = "tekst's \t\t tekst2'd"
		self.assertEqual(stu.string_to_upper(case),"Tekst's \t\t Tekst2'd")


if __name__ == '__main__':
    unittest.main()