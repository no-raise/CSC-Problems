# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
from typing import List

def max_sum_subarray(num_array: List[int]):
    if len(num_array) == 0:
        return 0

    n: int = len(num_array)
    max_sum: int = num_array[0]
    curr_sum: int = max_sum

    for i in range(1, n):
        curr_sum = max(num_array[i], curr_sum + num_array[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum 

if __name__ == "__main__":
    test_array1: List[int] = [-2, -3, 4, -1, -2, 1, 5, -3]
    test_array2: List[int] = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
    
    print(max_sum_subarray(test_array1))
    print(max_sum_subarray(test_array2))

    