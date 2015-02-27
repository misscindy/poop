"""

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]



"""


def partition(s):

    def _partition(rest, partial, result):
        if not rest:
            result.append(partial[:])
            return

        for i in range(len(rest)):
            nxt, remaining = rest[:i + 1], rest[i+1:]
            if is_pal(nxt):
                partial.append(nxt)
                _partition(remaining, partial, result)
                partial.pop()

    res = []
    _partition(s, [], res)
    return res

def is_pal(s):
    return is_palindrome(s, 0, len(s) - 1)


def is_palindrome(s, left, right):
    if left >= right:
        return True
    return s[left] == s[right] and is_palindrome(s, left + 1, right - 1)


if __name__ == '__main__':
    test_cases = [
        ("aaaa", True),
        ("aaa", True),
        ("ab", False),
        ("121", False),

    ]
    for test_case, exp in test_cases:
        # print is_palindrome(test_case, 0, len(test_case) - 1) == exp
        print partition(test_case)





