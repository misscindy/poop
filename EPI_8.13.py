from util import *

def zip(linked_list):
    def helper(head, cur, next):
        if not next:
            return head, cur
        head, node = helper(head, next, next.next)
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




if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7]
    printLinkedList(zip(createLinkedList(values)))






