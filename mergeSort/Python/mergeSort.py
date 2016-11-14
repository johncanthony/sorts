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
	        _listL = []
                _listR = []
                listLen=len(_list)
                
                """ Return list if the length is 0 or 1"""
                if(listLen<=1):
                    return(_list)

                if(listLen>1):
			splitpos=int(listLen/2)
                        
                        _listR = _list[splitpos:]
                        _listL = _list[:splitpos]
                       
                        left = self.run_sort(_listL)
                        right = self.run_sort(_listR)

                return self.run_merge(left,right)
                         
                        
		

	def run_merge(self,_listL,_listR):
		""" Merge the two lists back together in sorted order"""
                merged=[]
                
                while (len(_listL) > 0 and len(_listR) > 0):
                    if(_listL[0] == None):
                        merged.append(_listR.pop(0))
                        _listL.pop(0)
                    elif(_listL[0]>=_listR[0]):
                        merged.append(_listR.pop(0))
                    else:
                        merged.append(_listL.pop(0))

                while(len(_listL) > 0):
                        merged.append(_listL.pop(0))
                while(len(_listR) > 0):
                        merged.append(_listR.pop(0))

		return merged


