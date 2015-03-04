"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"


"""


def generate_parentheses(n):
    result = []

    def _helper(s, left, right):
        if left > n or right >= n:
            return
        if left == n:
            result.append(s + ")" * (n - right))
            return
        if left > right:
            _helper(s + ")", left, right + 1)
        _helper(s + "(", left + 1, right)

    _helper("", 0, 0)
    return result
        

if __name__ == '__main__':
    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    ]
    for test_case, exp in test_cases:
        print generate_parentheses(test_case)
        # print set(generate_parentheses(test_case)) == set(exp)





