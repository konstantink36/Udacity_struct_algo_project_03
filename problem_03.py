# Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers
# Chosen method: First sort list in decreasing order with merge sort algorithm.. Then construct two numbers by picking alternate indices from the sorted array.
# The code for merge sort is borrowed /adapted from classroom material.

def rearrange_digits(input_list):

    if input_list == None or len(input_list) == 0 :
        return -1, -1

    def mergesort(array):
        if len(array) > 1:

            #  divide array at point p
            p = len(array)//2
            left = array[:p]
            right = array[p:]

            # Sort the two halves
            mergesort(left)
            mergesort(right)

            i = j = k = 0

            # until end of either left or right is reached, put elements in right position
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            # when no more elements in left or right, pick up the remaining elements and put in array
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return array
       
    list_maxsort = mergesort(input_list)     # sort list in increasing order

    # 'a' is filled with numbers at the odd indices of the (decreasing order) sorted list
    a = ""
    for i in range(0,len(list_maxsort),2):
        a += str(list_maxsort[i])
 
    # `b` is filled with numbers at the even indices of the (decreasing order) sorted list
    b = ""
    for i in range(1,len(list_maxsort),2):
        b += str(list_maxsort[i])

    return int(a), int(b)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")



# Tests below

test_function([[1, 2, 3, 4, 5], [542, 31]])                     # prints Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])                 # prints Pass
test_function([[2,3,4,5,7,8,9,4,5,1,8,6], [986542, 875431]])    # prints Pass
test_function([None, [-1,-1]])                                  # prints Pass
test_function([[], [-1,-1]])            
