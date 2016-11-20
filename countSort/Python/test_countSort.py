import unittest
from countSort import * 


class TestCountSort(unittest.TestCase):

	test_1 = [[0,3,1],[0,1,3]]
	test_2 = [[5,2,6,1,1],[1,2,1,5,6]]
	test_3 = [[1,3,5,99,9,0,2,4,4],[0,1,2,3,4,4,5,9,99]]
        test_c_prime = [[1,1,0,1],[1,2,2,3]]
        sortObj=countSort()


        def test_countSort(self):
		"""Provide a length 3 list object populated with positive integers and check for correct sort """
		self.assertEqual(self.sortObj.run_sort(self.test_1[0]),self.test_1[1])
		
	def test_countSort2(self):
		"""Provide a length 5 list object populated with positive integers and prove correct sort through contradiction  """
		self.assertNotEqual(self.sortObj.run_sort(self.test_2[0]),self.test_2[1])

	def test_countSort3(self):
		""" Provide a length 8 list object populated with  positive integers and check for correct sort """
		self.assertEqual(self.sortObj.run_sort(self.test_3[0]),self.test_3[1])


        def test_run_c_prime(self):
                """ Provide a C list for count sort and return C` list """
	        self.assertEqual(self.sortObj.run_c_prime(self.test_c_prime[0]),self.test_c_prime[1])


if __name__ == '__main__':
	unittest.main()
	
