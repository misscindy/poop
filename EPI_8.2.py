# Reverse Linked List 


# Recursive, Non-Recursive, Stack 
from util import *


def reverse_ll(head):

	if not head: return None 
	head, _ = _reverse(head, head.next) 
	return head 


def _reverse(current, next):
	if not next: return current, current
	head, tail = _reverse(current.next, next.next)
	tail.next = current
	tail = current
	tail.next = None 
	return head, tail 


	




if __name__ == '__main__':
	values = [1, 3, 5, 7, 9]
	ll = createLinkedList(values)
	ll = createLinkedList(values, rand=True, uni=True, size=5)
	printLinkedList(ll)
	head = reverse_ll(ll)
	printLinkedList(head)



