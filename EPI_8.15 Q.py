from util import *

def check_palindrome(linked_list):
    def helper(head, cur, next):
        if not next:
            return head, cur, True
        head, node, result = helper(head, next, next.next)
        return head.next, cur, result and head.val == node.val

    if not linked_list: return None
    _, _, result = helper(linked_list, linked_list, linked_list.next)
    return result


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 1], False),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 1], True),
        ([1, 2, 3], False),
    ]

    print '\n', '=' * 20
    for test_case, expected in test_cases:
        print check_palindrome(createLinkedList(test_case)) == expected
    print




