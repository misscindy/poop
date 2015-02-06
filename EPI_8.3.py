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

    h, t, r = _reverse(prev.next, prev.next.next, counter + 1, n)
    prev.next = h
    t.next = r
    # tail.next = prev.next 
    # prev.next = prev_next
    return head 



def reverse_ll(head):

	if not head: return None 
	head, _ = _reverse(head, head.next) 
	return head 


def _reverse(cur_node, next_node, counter, n):
    if counter == n:
        return cur_node, cur_node, cur_node.next
    head, tail, r = _reverse(next_node, next_node.next, counter + 1, n)
    tail.next = cur_node
    tail = cur_node
    tail.next = None 
    return head, tail, r




if __name__ == '__main__':
    test_cases = [
        (([1, 3, 5, 7, 9], 2, 4), [1, 7, 5, 3, 9]),
        (([3, 5], 1, 2), [5, 3]),
    ]
    
    for ((values1, m, n), values2) in test_cases:
        l1, l2 = createLinkedList(values1), createLinkedList(values2)
        head = reverseBetween(l1, m, n)
        print isSameLinkedList(l1, l2)

	# values = [1, 3, 5, 7, 9]
	# ll = createLinkedList(values)
	# ll = createLinkedList(values, rand=True, uni=True, size=5)
	# printLinkedList(ll)
	# head = reverseBetween(ll, 2,4)
	# printLinkedList(head)





