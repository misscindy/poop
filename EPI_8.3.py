# Reverse a single sublist 
# Reverse the nodes from s-th node to f-th node 
# Numbering begins at 1 
# One single pass 
from util import * 

# def reverse_sublist(head, s, f):

def reverseBetween(head, m, n):
    if not head: return head 
    counter, prev, tail_next = 1, head, head
    while counter < m - 1:
        prev = prev.next
        counter += 1 
    
    prev_next, tail = _reverse(prev.next, prev.next.next, counter + 1, n)
    # tail.next = prev.next 
    # prev.next = prev_next 
    return head 



def reverse_ll(head):

	if not head: return None 
	head, _ = _reverse(head, head.next) 
	return head 


def _reverse(current, next, counter, n):
	if counter == n: 
		return current, current

	head, tail = _reverse(current.next, next.next, counter + 1, n)
	tail.next = current
	tail = current
	tail.next = None 
	return head, tail 




if __name__ == '__main__':
	values = [1, 3, 5, 7, 9]
	ll = createLinkedList(values)
	ll = createLinkedList(values, rand=True, uni=True, size=5)
	printLinkedList(ll)
	head = reverseBetween(ll, 2,4)
	printLinkedList(head)





