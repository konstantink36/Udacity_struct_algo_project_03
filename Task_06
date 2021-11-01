# Find Maximum and Minimum Element in array using divide and conquer method
# The array is divided in two halves, then using recursive approach to find maximum and mimum numbers in each half.
# Then return the maximum of the two maxima of each half and the mimimum of two minima of each half.


def maxmin(arr, first, last):
	     
    # if array has 1 element, return it as both min, max
    if (last - first) == 0 :  
        return arr[first], arr[first]

    # if array has 2 elements, return min max of the two
    if (last - first) == 1 :
        max = arr[last] if arr[first] < arr[last] else arr[first]
        min = arr[first] if arr[first] < arr[last] else arr[last]

    else : 
        mid = int(first + (last - first) / 2)               # midpoint to divide array into two halves
        min_left, max_left = maxmin(arr, first, mid)        # recursively search the left half
        min_right, max_right = maxmin(arr, mid, last)       # recursively search the right half
    
        max = max_left if max_left > max_right else max_right  # return the maximum of the two maxima of the left half
        min = min_left if min_left < min_right else min_right  # return the maximum of the two maxima of the right half

    return min, max


def get_min_max(ints) :
    if ints == []:
        return ()
    if ints == None :
        return None
    first_index = 0
    last_index = len(ints) -1
    mini, maxi = maxmin(ints, first_index, last_index)
    return  mini, maxi
    

# Tests below
            
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# prints Pass

import random
l = [i for i in range(0, 100000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")
# prints Pass

A = [ 15, 7, 4 , 30, 2, 12, 44, 13]
print(get_min_max(A))			
# prints (2, 44)

B = []
print(get_min_max(B))			
# prints ()

C = None
print(get_min_max(C))			
# sprints None
