
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
       raise ValueError("Empty List")
   if len(int_list) == 0:
       return(None)
   min=int_list[0]
   for i in int_list:
       if i > min:
           min=i
   return(min)
   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError("Empty List")
   if len(int_list)==0 or len(int_list)==1:
       return(int_list)
   else:
       return int_list[-1:] + reverse_rec(int_list[:-1])
   pass


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mididx = (low + high)//2
    if int_list is None:
        raise ValueError("Empty List")
    if target == int_list[mididx]:
        return mididx
    elif int_list[mididx] > target:
        if low <= high:
            return bin_search(target, low, mididx-1, int_list)
    elif int_list[mididx] < target:
        if low <= high:
            return bin_search(target, mididx+1, high, int_list)
    else:
       return None


