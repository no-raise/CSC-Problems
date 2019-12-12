# Write a method to replace all spaces in a string with '%2e: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

def URLify_pythonic(s: str) -> str:
    return s.replace(' ', '%20') 

def URLify_logical(s: str) -> str:
    res = []

    for char in s:
        if char == " ":
            res.append("%20")
        else:
            res.append(char)
    
    return ''.join(res)


if __name__ == "__main__":
    url = "Mr John Smith"
    print(URLify_logical(url))