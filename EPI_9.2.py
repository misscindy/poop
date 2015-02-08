# Evaluate RPN EX 


def evalRPN(tokens):
    ops = {"+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
              "/": lambda a, b: int(float(a) / b)}
    stack = []
    for i in tokens:
        if i in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[i](b, a))
        else:
            stack.append(int(i))
        print stack, i
    print stack
    return stack[0]
    
            
            
if __name__ == '__main__':
   	test_case = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]   
   	print evalRPN(test_case)