Problem 2:
Search for a number in sorted rotated array. Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

Implemented with binary search and recursive function call.
The array can be split in two parts where each part increases monotonically, so the problem can be solved with binary search.
Binary search has better time complexity O(log n) than linear search (O(n).

Time Complexity: O(log n)
Space Complexity: O(log n) for recursive function call stack
