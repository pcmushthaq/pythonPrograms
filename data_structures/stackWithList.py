class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        length = len(self.stack)
        if(length == 0):
            return
        return self.stack[length-1]

    def length(self):
        return len(self.stack)

    def isEmpty(self):
        return 0 == len(self.stack)


myStack = Stack()
myStack.push(1)
myStack.push('Hi')
myStack.push('Helloo')
print(myStack.peek())
print(myStack.stack)
myStack.pop()
print(myStack.stack)
