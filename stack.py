# Python implementation of stacks using linkedlists
# can be also done using lists, dequeues, queue.LifoQueue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peak(self):
        return self.top

    def printStack(self):
        values = []
        currentNode = self.top
        while currentNode is not None:
            values.append(currentNode.value)
            currentNode = currentNode.next
        print(values)

    def push(self, node: Node):
        if(self.length == 0):
            self.top = node
            self.bottom = node
            self.length += 1
        else:
            # We are adding to the beginning of LL
            # So that it will be easier to remove
            currentTop = self.top
            self.top = node
            self.top.next = currentTop
            self.length += 1

    def pop(self):
        if(self.length == 0):
            return
        elif self.length == 1:
            self.top = None
            self.bottom = None
            self.length -= 1
        else:
            follower = self.top.next
            self.top = follower
            self.length -= 1


myStack = Stack()
myStack.push(Node(1))
myStack.push(Node('Hi'))
myStack.push(Node('Helloo'))
print(myStack.peak().value)
myStack.printStack()
myStack.pop()
myStack.printStack()
