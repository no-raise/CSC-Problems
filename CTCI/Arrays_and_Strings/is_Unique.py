#  Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False

    from collections import defaultdict

    dict = defaultdict(bool)

    for char in s:
        if dict[char]:
            return False
        else:
            dict[char] = True
        
    return True


if __name__ == "__main__":
        print(is_unique("123asd"))