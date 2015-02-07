
from util import *
def zip(head):
	# 1 -> 2 -> 3 -> 4 -> 5 -> None 
	def _zip(left, cur, nxt):
		if not nxt:
			return left, cur 
			# returns first and last node 
		left, right = _zip(left, cur.next, nxt.next)
		
		if left == right or left.next == right:
			right.next = None
			return left, right 

		cur.next = None 
		next_left = left.next
		left.next = right
		right.next = next_left
		return next_left, cur 

	if not head or not head.next: return head 
	_zip(head, head, head.next)
	return head 

def zip2(head):
	slow = fast = head
	while fast and fast.next:
		slow, fast = slow.next, fast.next.next

	stack = []
	slow = slow.next if fast else slow

	while slow:
		stack.append(slow)
		slow = slow.next
	#stack[0].next = None	

	runner = head 
	print stack
	while stack:
		
		'''
		temp = runner.next 
		print "temp: ", temp
		runner.next = stack.pop()
		runner = runner.next 
		runner.next = temp 
		print runner, stack
		runner = runner.next 
		'''

		temp = runner.next
		runner.next = stack.pop()
		runner.next.next = temp
		runner = temp
	runner.next = None
		
	# print "runner: ", runner, stack 
	# if runner: runner.next = None
	return head 





if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    printLinkedList(zip2(createLinkedList(values)))

    print 

    values = [1]
    printLinkedList(zip2(createLinkedList(values)))



