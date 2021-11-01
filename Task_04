# Dutch National Flag Problem
# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    counter0 = 0
    counter1 = 0
    counter2 = 0
    
    for i in range(len(input_list)):
        if input_list[i] == 0 :
            counter0 += 1
        elif input_list[i] == 1 :
            counter1 += 1
        elif input_list[i] == 2 :
            counter2 += 1

    input_list = counter0 * [0] + counter1 * [1] +  counter2 * [2]

    return input_list
    
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
     

# Tests below

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])							
# prints [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2] Pass

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])		
# prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] Pass

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])				
# prints [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2] Pass

test_function([])											
# prints [] Pass

test_function([None])											
# prints [], Fail
