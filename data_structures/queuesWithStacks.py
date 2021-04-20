# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal
# queue (push, peek, pop, and empty).
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.outStack.pop()

    def move(self):
        """
        Moves the elements from inStack to outStack if
        outStack is empty
        """
        if(not self.outStack):
            while(self.inStack):
                self.outStack.append(self.inStack.pop())

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return bool(len(self.outStack) == 0 and len(self.inStack) == 0)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(10)
obj.push(15)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
