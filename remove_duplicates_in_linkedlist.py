
from utils import *

def remove_duplicates(linked_list):
    if not linked_list: return
    dummy = ListNode(-1)
    dummy.next = linked_list
    pre, current, next, duplicate = dummy, linked_list, linked_list.next, False
    while next:
        if current.val == next.val:
            duplicate = True
            if not next.next:
                pre.next = None
                break
            else:
                next = next.next
        else:
            if duplicate:
                duplicate = False
                pre.next = next
            else:
                pre = current
            current, next = next, next.next
    return dummy.next


def remove_duplicates2(linked_list):
    if not linked_list: return
    dummy = ListNode(-1)
    dummy.next = linked_list
    tail, left, right, cur = dummy, dummy, linked_list.next, linked_list
    while right:
        if cur.val not in (left.val , right.val):
            tail.next = cur
            tail = tail.next
        left, cur, right = cur, right, right.next
    # corner case, last ele
    tail.next = cur if cur.val != left.val else None
    return dummy.next


if __name__ == '__main__':
    values = [1, 1, 2, 3, 3, 3, 4, 7, 8, 5, 5, 5, 6]
    l = createLinkedList(values)
    printLinkedList(l)
    # head = remove_duplicates(l)
    head = remove_duplicates2(l)
    printLinkedList(head)




