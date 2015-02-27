"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

"""
# TODO: (alternative way)


def permute_unique(numbers):
    def _permute(sofar, rest, sol_set):
        if not rest:
            sol_set.append(sofar)
            return
        checked = set()
        for i in range(len(rest)):
            if rest[i] not in checked:
                next, remaining = sofar + [rest[i]], rest[:i] + rest[i + 1:]
                _permute(next, remaining, sol_set)
                checked.add(rest[i])


    numbers.sort()
    sofar, rest, sol_set = [], numbers, []
    _permute(sofar, rest, sol_set)
    return sol_set


if __name__ == '__main__':
    test_cases = [
        (([1, 2, 3]), ([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])),
        (([1, 1]), ([[1, 1]]))


    ]

    for test_case, exp in test_cases:
        print permute_unique(test_case), " == ",exp,
        print permute_unique(test_case) == exp



# http://fisherlei.blogspot.com/2012/12/leetcode-permutations-ii.html