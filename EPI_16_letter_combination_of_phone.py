"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

def possible_phone_num(digits):

    pad = [
        None, None,
        ("a", "b", "c"), ("d", "e", "f"),
        ("g", "h", "i"),("j", "k", "l"),
        ("m", "n", "o"),("p", "q", "r", "s"),
        ("t", "u", "v"), ("w", "x", "y", "z")
    ]

    def _possible_num(sofar, rest, result):
        if not rest:
            result.append(sofar)
            return

        for c in pad[int(rest[0])]:
            nxt, remain = sofar + c, rest[1:]
            _possible_num(nxt, remain, result)

    result = []
    _possible_num("", digits, result)
    return result


if __name__ == '__main__':
    test_cases = [
        ("2", ["a", "b", "c"]),
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]

    for test_case, exp in test_cases:
        print possible_phone_num(test_case), " == ", exp,
        print possible_phone_num(test_case) == exp
