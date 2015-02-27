# Find line through the most points

# let p be a set of n points on a plane


def find_line(p):
    tangents = {}
    # {k : points}

    for ndx, (a, b) in enumerate(p):
        for (c, d) in p[ndx + 1:]:
            k = 0 if not (a - c) else (b - d)/float(a - c)
            if k in tangents:
                tangents[k].add((a, b))
                tangents[k].add((c, d))
            else:
                tangents[k] = set([(a, b), (c, d)])
            # n^2
    max_line, max_points, key = None, 0, None
    for (k, line) in tangents.items():
        if len(line) > max_points:
            max_line, max_points, key = line, len(line), k

    return max_line, max_points, k

if __name__ == '__main__':
    test_cases = [
        ([(1, 1), (2, 3), (1, 2), (5, 6)]),

        ]

    for test_case in test_cases:
        print find_line(test_case)






