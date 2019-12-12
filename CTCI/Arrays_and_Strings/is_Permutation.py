# Given two strings, write a method to decide if one is a permutation of the
# other.

from collections import Counter

def is_Permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    word_count = Counter()

    for letter in s1:
        word_count[letter] += 1
    
    for letter in s2:
        word_count[letter] -= 1
        if word_count[letter] < 0:
            return False
    
    return True

if __name__ == "__main__":
    s1 = "absds2"
    s2 = "badsss"

    print(is_Permutation(s1, s2))
    