# Find the nearest repeated entry in an array
# Write a function which finds the distance of any closest pair of equal entries
import sys


def find_closest_pair(strings):
    closest_dist = sys.maxint
    last_seen = {}
    # {string : last_seen_index}
    for ndx, string in enumerate(strings):
        if string in last_seen:
            diff = ndx - last_seen[string]
            closest_dist = min(diff, closest_dist)
            last_seen[string] = ndx
        else:
            last_seen[string] = ndx
    return -1 if closest_dist == sys.maxint else closest_dist


if __name__ == '__main__':
    test_cases = [
        (["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "results"], 2),
        ("Write a function which finds the distance of any closest pair equal entries".split(), -1)

    ]
    for test_case, exp in test_cases:
        print find_closest_pair(test_case), " == ", exp