Problem 3:
Rearrange Array Elements so as to form two numbers such that their sum is maximum. 
For e.g. [1, 2, 3, 4, 5] the expected answer would be [531, 42]

Implemented with merge sort (Divide and conquer method)
First sort list in decreasing order with merge sort. Then construct two numbers by picking alternate indices from the sorted array.
Merge sort meets the requirement of O(n log n) time complexity. It could also have been heap sort.

Time Complexity: O(n log n)
Space Complexity: O(n)
