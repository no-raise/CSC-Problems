def is_one_away(s1, s2):
    if len(s1) == len(s2):
        edit_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                edit_count += 1
            if edit_count > 1:
                return False
        return edit_count == 1

    elif len(s1) > len(s2) and (len(s1) - len(s2)) == 1:
        return is_one_away_helper(s1, s2)
        
    elif len(s2) > len(s1) and (len(s2) - len(s1)) == 1:
        return is_one_away_helper(s2, s1)
    
def is_one_away_helper(s1, s2):
    shift = False
    for i in range(len(s1) - 1):
        if not shift:
            if s1[i] != s2[i]:
                shift = True
                if s1[i+1] != s2[i]:
                    return False   
        else:
            if s1[i+1] != s2[i]:
                return False
    return True


if __name__ == "__main__":
    s1 = 'pale'
    s2 = 'bae'

    print(is_one_away(s1, s2))

