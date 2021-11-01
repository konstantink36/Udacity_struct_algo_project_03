# Find the floored square root of a number with binary search
# Args: number(int): Number to find the floored squared root. Returns: int: Floored Square Root

def sqrt(number):
    if (number == 0 or number == 1):
        return number

    # iterative binary search with while loop to find floor sqrt(number)
    first = 1
    last = number

    while (first <= last):
        x = int(first + (last - first)/2)  # midpoint of search range

    # if x * x is perfect square, return x
        if (x * x) == number :
            return x
        
    # if (x * x) is smaller than number, search on the right side of x and store the result
        elif (x * x) < number :
            first = x + 1
            result = x

    # if (x * x) is larger than number, search on the left side of x
        elif (x * x) > number :
            last =  x - 1
            result = x

    return result


# Tests below

print(sqrt(9))   	# prints 3
print(sqrt(0))   	# prints 0
print(sqrt(81))  	# prints 9
print(sqrt(1))   	# prints 1
print(sqrt(17))  	# prints 4
print(sqrt(1000000))    # prints 1000
