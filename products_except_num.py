# Given an array nums of n integers where n > 1, return an array outpuy
# such that output[i] is equal to the product of all the elements of nums except nums[i].
from typing import List

def product_except_self(nums_array: List[int]) -> List[int]:
    n: int = len(nums_array)
    result: List[int] = [0] * n
    
    #product to left of first element is always 1
    result[0] = 1

    # to finding left product we start at second index because we know the value of
    # product for first index
    for i in range(1, n):
        result[i] = nums_array[i - 1] * result[i - 1]
    
    #similarly initializing right product
    right_product: int = 1
    for i in reversed(range(n)):
        result[i] *= right_product
        right_product *= nums_array[i]

    return result

if __name__ == "__main__":
    test_array1: List[int] = [1,2,3,4]
    print(product_except_self(test_array1))
