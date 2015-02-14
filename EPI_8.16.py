# Given a circular list: 
# Return the median 

from util import * 

def find_median(head):
	# find first non-increasing node
	min_start = head
	while min_start:
		if min_start.next.val < min_start.val:
			min_start = min_start.next 
			break 
		min_start = min_start.next 
	slow = fast = min_start
	while fast.next != min_start and fast.next.next != min_start:
		print fast
		slow = slow.next 
		fast = fast.next.next 
	print slow

	if fast.next.next == min_start:
		median = (slow.val + slow.next.val)/2.0
	else: 
		median = slow.next.val 

	return median 

def print_circular(head):
	runner = head 
	print head, 
	while runner.next not in (head, None):
		print runner.next,
		runner = runner.next 
	print runner.next 



if __name__ == '__main__':
	
	head = ListNode(0)
	runner = head 
	for i in range(5,10):
		runner.next = ListNode(i)
		runner = runner.next 
	runner.next = head 
	#printLinkedList(head)
	print_circular(head.next.next)

	print find_median(head.next.next)

w





		