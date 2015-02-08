# copy a posting list 
# Linked list with random pointers 

#Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

    def __repr__(self):
    	rand = self.random.val 
    	return "Node(%i): %i -> " % (rand, self.val)


def copy_posting(head):
	dummy = RandomListNode(-1)
	runner, used = dummy, {}

	while head:
		# new_node
		if head in used: new_node = used[head]
		else: 
			new_node = RandomListNode(head.val)
			used[head] = new_node

		# random
		if head.random:
			if head.random in used:
				new_random = used[head.random]
			else:
				new_random = RandomListNode(head.random.val)
				used[head.random] = new_random
			new_node.random = new_random

		runner.next = new_node
		head, runner = head.next, runner.next 
	return dummy.next 


if __name__ == '__main__':
	# random list 
	head = RandomListNode(0)
	first = RandomListNode(1)
	sec = RandomListNode(2)
	third = RandomListNode(3)
	head.next, head.random = first, sec
	first.next, first.random = sec, head
	sec.next, sec.random = third, third
	third.next, third.random = None, sec
	runner = head
	while runner:
		print runner,
		runner = runner.next

	print
	new_head = copy_posting(head)
	while new_head:
		print new_head,
		new_head = new_head.next
	



		
