import unittest
from fib import *

class TestSorts(unittest.TestCase):

	def test_fib(self):
		sequence_number = 3
		start_pointa=0
		start_pointb=1
		expected_result = 1
		self.assertEqual(fib(sequence_number,start_pointa,start_pointb),expected_result)

	def test_fib2(self):
		sequence_number = 10
		start_pointa=0
		start_pointb=1
		expected_result =  34
		self.assertEqual(fib(sequence_number,start_pointa,start_pointb),expected_result)

if __name__ == '__main__':
	unittest.main()

