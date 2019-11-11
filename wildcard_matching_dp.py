# match a pattern to a string
# * matches any sequence of chars
# . matches only one char


def is_match(s: str, pattern: str) -> bool:
    memo = {}

    def dp_solution(i: int, j: int) -> None:
        # i represents an index in the string, j represents index in pattern
        # ans = False
        if (i, j) not in memo:
            # if we are last char of the pattern
            if j == len(pattern):
                memo[i, j] = i == len(pattern)
            else:
                # check current match
                if i < len(s):
                    match = pattern[j] in [s[i], '.']

                    # now we check next symbol in pattern
                if j + 1 < len(pattern):
                    if pattern[j+1] == '*':
                        memo[i, j] = dp_solution(
                            i, j+2) or match and dp_solution(i+1, j)
                    else:
                        memo[i, j] = match and dp_solution(i+1, j+1)
        return memo[len(s)-1, len(pattern)-1]

    return dp_solution(0, 0)


if __name__ == "__main__":
    print(is_match('aa', 'a'))
    print(is_match('aa', '*'))
    print(is_match('ab', '.*'))
