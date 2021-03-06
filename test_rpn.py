import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 + ')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_multiply(self):
		result = rpn.calculate('4 3 *')
		self.assertEqual(12, result)
	def test_divide(self):
		result = rpn.calculate('12 3 /')
		self.assertEqual(4, result)
	def test_div_by_0(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('4 0 /')
	def test_factorial(self):
		result = rpn.calculate('4 !')
		self.assertEqual(24, result)
	def test_int_division(self):
		result = rpn.calculate('13 3 .')
		self.assertEqual(4, result)
	def test_exponent(self):
		result = rpn.calculate('3 2 ^')
		self.assertEqual(9, result)