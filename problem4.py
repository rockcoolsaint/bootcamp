import unittest, fibonacci

class FibonacciTest(unittest.TestCase):
	def testPositiveFibonacci(self):
		self.assertEqual(fibonacci.fibonacci(5), [0,1,1,2,3], msg="5 fibonacci should return [0,1,1,2,3]")
		self.assertEqual(fibonacci.fibonacci(4), [0,1,1,2], msg="4 factorial should return [0,1,1,2]")
		self.assertEqual(fibonacci.fibonacci(3), [0,1,1], msg="3 factorial should return [0,1,1]")
	
	def testNegativeFibonacci(self):
		self.assertEqual(fibonacci.fibonacci(-9), -1, msg="Fibonacci of a negative number should return false")

	def testAlphabeticalInput(self):
		self.assertEqual(fibonacci.fibonacci('ieiee'), -1,  msg="Fibonacci should return false for alphatical input")

	def testDecimalInput(self):
		self.assertEqual(fibonacci.fibonacci(2.3453), -1,  msg="Fibonacci should return false for a decimal number")

	def testVariousTypesInputs(self):
		self.assertEqual(fibonacci.fibonacci(1a2j3), -1,  msg="Fibonacci should return false for a various datatype input")

	def testListInputs(self):
		self.assertEqual(fibonacci.fibonacci([1]), -1,  msg="Fibonacci should return false for a list input")

	def testIfNotEven(self):
		self.assertEqual(fibonacci.fibonacci(4, "odd"), -1,  msg="Fibonacci should return false for a list input")

	def testIfNotOdd(self):
		self.assertEqual(fibonacci.fibonacci(4, "even"), -1,  msg="Fibonacci should return false for a list input")

if __name__ == '__main__':
	unittest.main()