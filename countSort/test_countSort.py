import unittest
from countSort import * 


class TestCountSort(unittest.TestCase):

	test_1 = [[0,3,1],[0,1,3]]
	test_2 = [[5,2,6,1,1],[1,2,1,5,6]]
	test_3 = [[-1,3,5,99,0,2,4,4],[-1,0,2,3,4,4,5,99]]


        def test_max_num(self):
                """ Provide a list of integers and return the largest integer in the list"""
                sortObj=countSort()
                self.assertEqual(sortObj.get_c_length(self.test_3[0]),100)
       
        def test_build_c_list(self):
                sortObj=countSort()
                self.assertEqual(sortObj.build_c_list(3),['a','a','a'])

        def test_countSort(self):
		"""Provide a length 3 list object populated with positive integers and check for correct sort """
		sortObj=countSort()
		self.assertEqual(sortObj.run_sort(self.test_1[0]),self.test_1[1])
		
	def test_countSort2(self):
		"""Provide a length 5 list object populated with positive integers and prove correct sort through contradiction  """
		sortObj=countSort()
		self.assertNotEqual(sortObj.run_sort(self.test_2[0]),self.test_2[1])

	def test_countSort3(self):
		""" Provide a length 8 list object populated with  positive and negative integers and check for correct sort """
		sortObj=countSort()
		self.assertEqual(sortObj.run_sort(self.test_3[0]),self.test_3[1])


		
if __name__ == '__main__':
	unittest.main()
	
