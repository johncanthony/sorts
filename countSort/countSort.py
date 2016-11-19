class countSort():

    def run_sort(self,_list):
       
        c_length=self.get_c_length(_list)
        c_list = build_c_list(c_length)
        c_prime = build_c_list(c_length)

        count = 0

        for each in _list:
            if (c_list[each] == 'a'):
                c_list[each] = 1
            c_list[each] += 1

            
            

        return _list 

    def get_c_length(self,_list):
        """ Get the length of the C list and take into account negative numbers """ 
        max_num = 0
        min_num = 0

        for each in _list:
            if each > max_num:
                max_num = each 
            if each < min_num:
                min_num = each

        return max_num + abs(min_num) 

    def build_c_list(self,c_length):
        """ Build list of 'a' from length of c list """
        c_list = ['a'] * c_length

        return c_list
