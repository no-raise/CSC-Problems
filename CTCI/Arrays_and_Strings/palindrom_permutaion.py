# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.

def is_palindrome_permutaion(s: str) -> bool:
    from collections import Counter

    word_count = Counter()
    odd_count = 0

    for letter in s.lower():
        if ord('a') <= ord(letter) <= ord('z'):
            word_count[letter] += 1
    
    for count in word_count.values():
        if count % 2 == 1:
            odd_count += 1

    return odd_count <= 1

if __name__ == "__main__":
    test = 'ssws'
    print(is_palindrome_permutaion(test))

