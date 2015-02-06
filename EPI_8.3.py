# Reverse a single sublist 
# Reverse the nodes from s-th node to f-th node 
# Numbering begins at 1 
# One single pass 
from util import * 

# def reverse_sublist(head, s, f):


def reverseBetween(head, m, n):
    if not head or n == m: return head 
    dummy = ListNode(-1)
    dummy.next = head 
    counter, prev = 1, dummy
    while counter < m:
        prev = prev.next
        counter += 1 
    
    h, t, r = _reverse(prev.next, prev.next.next, counter + 1, n)
    prev.next = h
    t.next = r 
    return dummy.next 
    
def _reverse(current, nxt, counter, n):
    if counter == n + 1:
        return current, current, nxt 
    head, tail, remainder = _reverse(current.next, nxt.next, counter + 1, n)
    tail.next = current
    tail = tail.next 
    current.next = None 
    return head, tail, remainder  
    
    

if __name__ == '__main__':
    test_cases = [
        (([1, 3, 5, 7, 9], 2, 4), [1, 7, 5, 3, 9]),
        (([3, 5], 1, 2), [5, 3]),
    ]
    
    for ((values1, m, n), values2) in test_cases:
        l1, l2 = createLinkedList(values1), createLinkedList(values2)
        head = reverseBetween(l1, m, n)
        printLinkedList(head)
        printLinkedList(l2)
        print isSameLinkedList(head, l2)

	# values = [1, 3, 5, 7, 9]
	# ll = createLinkedList(values)
	# ll = createLinkedList(values, rand=True, uni=True, size=5)
	# printLinkedList(ll)
	# head = reverseBetween(ll, 2,4)
	# printLinkedList(head)





