class sorts(object):
     @staticmethod
     def bubbleSort (array, swaps):
            swap = 0
            for i in range(0, len(array) - 1):
               if array[i] > array[i+1]:
                  store = array[i]
                  array[i] = array[i+1]
                  array[i+1] = store
                  swap += 1
            
            if swap == 0:
               return array
            else:
               swaps += swap
               sorts.bubbleSort(array, swaps)
               return array
