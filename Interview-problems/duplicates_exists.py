# We find if the given array has any duplicates. 

from typing import List

def contains_duplicates(num_array: List[int]) -> bool:
    return len(set(num_array)) < len(num_array)

if __name__ == "__main__":
    test_array1: List[int] = [1, 2, 3, 4, 5, 6, 7]
    test_array2: List[int] = [1, 2, 3, 4, 5, 6, 7, 2, 4, 6]

    print(contains_duplicates(test_array1))
    print(contains_duplicates(test_array2))