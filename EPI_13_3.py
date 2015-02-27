# Given L and M: check if L can be rewritten by M


# Idea: Hashtable, process L -> check against M
# Idea2: ASCII code: use an array of length 256


# Idea: Hashtable, process L -> check against M


def rewrite(L, M):

    count_dict = dict()
    for i in L:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print count_dict
    for c in M:
        if c in count_dict:
            count_dict[c] -= 1
            if count_dict[c] == 0:
                count_dict.pop(c)
        else:
            break

    return len(count_dict) == 0


if __name__ == '__main__':
    test_cases = [
        (("abcdseeee","abcseeeed"), True),
        (("abfhkjacdseeee","abcseeefddsaed"), False),
        (("aa","a"), False),
        ]

    for test_case, exp in test_cases:

        print rewrite(test_case[0], test_case[1]) == exp








