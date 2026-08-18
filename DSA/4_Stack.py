class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, value):
        self.s.append(value)

    def pop(self):
        if self.length() == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop()

    def peek(self):
        if self.length() == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[self.length() - 1]

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.pop())
print(stk.peek())