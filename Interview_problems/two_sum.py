# We have to find to numbers in an array that add up to a given sum. 
# it is assumed that every input has one and only one solution and that 
# we cannot reuse the same number.
from typing import List, Dict

def two_sum(num_array: List[int], target: int) -> List[int]:
    seen: Dict[int] = {}
    for i, num in enumerate(num_array):
        if target - num in seen.keys():
            return [num_array[seen[target - num]], num]
        else:
            seen[num] = i
    
    return "No such combination was found."
    

if __name__ == "__main__":
    num_array = [2, 7, 11, 15]
    target = 13

    print(two_sum(num_array, target))
