class insertSort():

	def run_sort(self,_list):
		for x in range(1,len(_list)):
			k=x
			while(k>0):
				if(_list[k] <  _list[k-1]):
					q=_list[k]
					_list[k] = _list[k-1]
					_list[k-1] = q
				k=k-1
		return _list 
