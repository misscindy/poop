from util import *

def zip(linked_list):
    def helper(head, cur, next):
        if not next:
            return head, cur
        head, node = helper(head, next, next.next)
        # Odd nodes
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 5 -> 2 -> 4 -> 3
        # 
        # Even nodes
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 1 -> 6 -> 2 -> 5 -> 3 -> 4
        if head == node or head.next == node:
            node.next = None
            return head, node
        head_next = head.next
        head.next = node
        node.next = head_next
        return head_next, cur

    if not linked_list: return None
    helper(linked_list, linked_list, linked_list.next)
    return linked_list


def zip2(linked_list):
    slow_runner, fast_runner, i = linked_list, linked_list, 0
    while fast_runner.next and fast_runner.next.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        i += 1
    # i odd -> even nodes, i even -> odd nodes
    if i & 1:
        slow_runner = slow_runner.next

    stack = []
    while slow_runner:
        stack.append(slow_runner)
        slow_runner = slow_runner.next

    head, runner = linked_list, linked_list
    for node in reversed(stack):
        runner_next = runner.next
        runner.next = node
        node.next = runner_next
        runner = runner_next
    runner.next = None
    return head


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]

    print '\n', '=' * 10, 'Zip()', '=' * 10
    for test_case, expected in test_cases:
        origin = createLinkedList(test_case)
        zipped = zip(origin)
        print isSameLinkedList(zipped, origin), 
        printLinkedList(zipped)

    print '\n', '=' * 10, 'Zip2()', '=' * 10

    for test_case, expected in test_cases:
        origin = createLinkedList(test_case)
        zipped = zip2(origin)
        print isSameLinkedList(zipped, origin), 
        printLinkedList(zipped)

    print '\n'







