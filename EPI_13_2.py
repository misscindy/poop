# Whether the letters forming a string s can be permuted to form a palindrome
# edified

# TODO(bfan): Alternate solution
def permute_palindrome(s):
    used = set()
    for i in s:
        if i in used:
            used.remove(i)
        else:
            used.add(i)
    return len(used) <= 1




if __name__ == '__main__':
    test_cases = [
        [("ababa"),True],
        [("aa"),True],
        [("aba11"),True],


    ]
    for test_case, exp in test_cases:
        print permute_palindrome(test_case[0]) == exp