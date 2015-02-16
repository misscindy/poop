from util import *

def copy(head):
    h = head
    while head:
        node = ListNode(head.val)
        head_next = head.next
        head.next = node
        node.next = head_next
        head = head_next
    return h


def copy_linkedlist(head):
    dummy = ListNode(0)
    runner = dummy
    while head:
        runner.next = ListNode(head.val)
        head, runner = head.next, runner.next
    return dummy.next

def copy_poop(head):
    dummy = ListNode(0)
    runner = dummy
    while head:
        runner.next = ListNode(head.val)
        head, runner = head.next, runner.next 
    return dummy.next 

if __name__ == '__main__':
    values = []
    # linked_list = copy(createLinkedList(values))  # 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4
    linked_list = copy_poop(createLinkedList(values))  # 1 -> 2 -> 3 -> 4
    printLinkedList(linked_list)