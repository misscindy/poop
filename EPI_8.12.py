from utils import *

def zip(linked_list):
    def helper(head, cur, next):
        if not next:
            return cur
        node = helper(head, next, next.next)

        head_next = head.next
        head.next = node
        node.next = head_next
        return 

    if not linked_list: return None
    helper(linked_list, linked_list)
    return linked_list



if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    printLinkedList(zip(createLinkedList(values)))