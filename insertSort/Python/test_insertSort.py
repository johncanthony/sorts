import unittest
from insertSort import *

class TestinsertSort(unittest.TestCase):

	def test_insertSort(self):
		inVal=[0,3,1]
		self.assertEqual(insertSort.run_sort(inVal),[0,1,3])

if __name__ == '__main__':
	unittest.main()
	
