###########################################################
#  mergeSort()
#
#  johncanthony  11.13.16
#
#  Desc:
#	Implementaiton of mergeSort for algorithms study
#
###########################################################


class mergeSort():

	def run_sort(self,_list):
		""" Sort a list of integers and return the sorted list """
	 	listLen=len(_list)
		if(listLen>1):
			splitpos=int(listLen/2)
			left=self.run_sort(_list[:splitpos])
			right=self.run_sort(_list[splitpos:])
			print(left)
			print(right)
			print("====")
		return _list 

	def run_merge(self,_listL,_listR):
		merged=[]
		
		return merged
