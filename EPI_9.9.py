# Sort a stack 
# Ops: push, pop, top
# Sort stack in a desending order 

# top of the stack is the largest 

def sort(stack):
    # [1, 2, 3, 4]
    # top

    def _sort(stack, last):

        if len(stack) <= 1:
            _insert(last, stack)

        else:
            top = stack.pop()
            _sort(stack, top)
            _insert(top, stack)

    def _insert(top, stack):
        if len(stack) <= 1:
            if top > stack[0]:
                stack.append(top)
            else:
                stack.insert(0, top)
            return
        else:
            if top > stack[-1]:
                stack.append(top)
                return
            else:
                last = stack.pop()
                _insert(top, stack)
                stack.append(last)

    top = stack.pop
    _sort(stack, top)


if __name__ == '__main__':
    ls = [1, 5, 3, 5, 7, 4, 3]
    sort(ls)

    print ls



