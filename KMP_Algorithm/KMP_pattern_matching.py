def get_pi_table(pattern: str):
    # lps = [0] * len(s)
    # for i in range(1, len(s)):
    #     j = lps[i - 1]
    #     while j > 0 and s[i] != s[j]:
    #         j = lps[j - 1]
    #     if s[i] == s[j]:
    #         j += 1
    #     lps[i] = j

    n = len(pattern)
    i, j = 1, 0
    lps = [0] * n
    while i < n:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
            

    return lps

if __name__ == "__main__":
    lps = get_pi_table("abcadab")
    print(lps)