"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end,
such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""

from collections import deque


def word_ladder(start, end, dicty):
    queue = deque()
    alphabet = {chr(i) for i in range(97, 113)}
    queue.append([start, 1])
    used = set()
    used.add(start)

    while queue:
        word, level = queue.popleft()
        for i in range(len(word)):
            for c in alphabet:
                next = word[:i] + c + word[i + 1:]
                if next == end:
                    return level + 1
                if next in dicty and next not in used:
                    queue.append([next, level + 1])
                    used.add(next)
            # print queue
    return 0





if __name__ == '__main__':
    print word_ladder("hit", "cog", {"hot", "dot", "dog", "lot", "log"})
