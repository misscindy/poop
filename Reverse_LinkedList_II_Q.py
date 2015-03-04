
from util import *

def reverse_mn(ll, m, n):
    def reverse(node, m, n, pos):
        if pos == n or pos == n + 1:
            return node, node.next
        reversed_nodes, tail_nodes = reverse(node.next, m, n, pos + 1)
        if pos > m:
            node.next.next = node
            node.next = None
        elif pos == m:
            node.next.next = node
            node.next = tail_nodes
        elif pos == m - 1:
            node.next = reversed_nodes
        return reversed_nodes, tail_nodes
    dummy = ListNode(0)
    dummy.next = ll
    reversed_nodes, _ = reverse(ll, m, n, 1) if ll else (None, None)
    return dummy.next if m != 1 else reversed_nodes
    

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 1, 4, [4, 3, 2, 1, 5]),
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
        ([1, 2], 1, 2, [2, 1]),
        ([1], 1, 1, [1]),
        ([], 0, 0, []),
    ]
    for test_case, test_m, test_n, exp in test_cases:
        linked_list = createLinkedList(test_case)
        linked_list = reverse_mn(linked_list, test_m, test_n)
        exp_linked_list = createLinkedList(exp)
        print linked_list == exp_linked_list or isSameLinkedList(linked_list, exp_linked_list)


