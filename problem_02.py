# Given is a sorted array which is rotated at some random pivot point, example [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
# Search for a target number. If found in the array return its index, otherwise return -1.
# Implemented with binary search and recursive function call


def binary_search(input_list, start_index, end_index, number):
  
    
    x = int(start_index + (end_index - start_index) / 2)  # pivot in center of array

    if (start_index > end_index):
        return -1

    if input_list[x] == number :        
        return x

    # if search is in the sorted left part and the target is smaller than the pivot value, continue search in the left part
    if input_list[start_index] <= number <= input_list[x] :
        return binary_search(input_list, start_index, x - 1, number)

    # if search is in the sorted right part and the target is larger than the pivot value, continue search in the right part
    elif input_list[x] <= number <= input_list[end_index] :
        return binary_search(input_list, x + 1, end_index, number)

   # if the right part is unsorted, keep searching in the right part
    elif input_list[x] >= input_list[end_index] :
        return binary_search(input_list, x + 1, end_index, number)
    
    # if the left part is unsorted, keep searching in the left part
    elif input_list[start_index] >= input_list[x] :
        return binary_search(input_list, start_index, x - 1, number)

    return -1;

def rotated_array_search(input_list, number):
  return binary_search(input_list, 0, len(input_list)-1, number)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Tests below

print ("Test 1:")
a = [4,5,6,7,0,1,2]
print(rotated_array_search(a, 0))     # prints '4'

print ("Test 2:")
b = [6,7,8,9,10,11,12,2,3,4,5]
print(rotated_array_search(b, 12))    # prints '6'
print(rotated_array_search(b, 2))     # prints '7'
print(rotated_array_search(b, 3))     # prints '8'
print(rotated_array_search(b, 33))    # prints '-1'

print ("Test 3:")
c = []
print(rotated_array_search(c, 0 ))    # prints '-1'


print ("Test 4:")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])    # prints Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])    # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])           # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])           # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])          # prints Pass
