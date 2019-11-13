# find if a string consists of a substring repeated many times

def is_repeating_substring(pattern: str) -> bool:
    s: str = (pattern + pattern)[1:-1]
    if s.find(pattern) > -1:
        return True
    else:
        return False

if __name__ == "__main__":
    #Testing function
    s1: str = "ababab"
    s2: str = "avdsd"

    print(is_repeating_substring(s1))
    print(is_repeating_substring(s2))