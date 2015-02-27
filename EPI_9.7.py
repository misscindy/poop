class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None
        self.order = -1

    def __repr__(self):
        rand = self.random.val
        return "Node(%i): %i " % (rand, self.val)


def jump_order(head):
    counter, stack = 0, [head]
    while stack:
        current = stack.pop()
        if current and current.order == -1:
            current.order = counter
            counter += 1
            stack.append(current.next)
            stack.append(current.random)


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
    # runner = head
    # while runner:
    # print runner,
    # 	runner = runner.next

    # print
    jump_order(head)
    runner = head
    while runner:
        print runner, "order : ", runner.order
        runner = runner.next



		
