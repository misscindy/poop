# Linked List 
# Test Palindromicity 

from util import *
def isPalindrome(head):
	def _isP(front, cur, nxt):
		if not nxt:
			return front, cur, True
		front, back, status = _isP(front, cur.next, nxt.next)
		if status: 
			if front == back: return front, back, True
			nxt_front = front.next
			if front.val != back.val:
				return front, back, False
			return nxt_front, cur, True
		else:
			return None, None, False
	return _isP(head, head, head.next)

if __name__ == '__main__':
	
	values = [1]
	ll = createLinkedList(values)
	ll = createLinkedList(values, uni=True, size=5)
	printLinkedList(ll)
	head = isPalindrome(ll)
	print head



