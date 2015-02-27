# implement queue using stacks 


class Queue:
    # class Underflow(Exception)


    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            # transfer
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            # Todo: (BFan) throw exception
            return "What!!"

        return self.stack2.pop()

    def __repr__(self):
        return "%s, %s" % (self.stack1, self.stack2)


if __name__ == '__main__':
    aQ = Queue()
    for i in range(10):
        aQ.enqueue(i)
    print aQ

    for i in range(10, 1, -1):
        print aQ.dequeue()
        print aQ





