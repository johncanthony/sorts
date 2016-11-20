###########################################################
#  countSort()
#
#  johncanthony  11.19.16
#
#  Desc:
#   Implementaiton of countSort for algorithms study
#
###########################################################

class countSort():

    def run_sort(self,_list):
        """ Sort list of positive integers using the countSort Algorithm"""
        _sorted = [0] * len(_list) #Build empty sorted list
        c_length = max(_list) + 1  #Find Max number in list and add 1
        c_list = [0] * c_length    #Build empty c list 


        """ Populate c list from provided unsorted list"""
        for number in _list:
            c_list[number] += 1

            
        c_list   = self.run_c_prime(c_list)

        """ Populate sorted list"""
        for each in _list:
            _sorted[c_list[each]-1]= each
            c_list[each]-=1


        return _sorted


    def run_c_prime(self,c_list):
        """ Build C` list by summing the x and x-1 elements of the list """
        for i in range(1,len(c_list)):
            c_list[i] = c_list[i-1] + c_list [i]

        return c_list



