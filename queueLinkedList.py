from queue import Queue


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CustomQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def printQueue(self):
        values = []
        currentNode = self.first
        while currentNode is not None:
            values.append(currentNode.value)
            currentNode = currentNode.next
        print(values)

    def enqueue(self, node: Node):
        if(self.length == 0):
            self.first = node
            self.last = node
            self.length += 1
        else:
            # We are adding to the end of LL
            # So that it will be easier to remove the first item
            self.last.next = node
            self.last = node
            self.length += 1

    def dequeue(self):
        if(self.length == 0):
            return
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
        else:
            follower = self.first.next
            self.first = follower
            self.length -= 1


myQueue = CustomQueue()
myQueue.enqueue(Node(1))
myQueue.enqueue(Node('Hi'))
myQueue.enqueue(Node('Helloo'))
print(myQueue.peek().value)
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()

# Built in method
newQueue = Queue(maxsize=5)
newQueue.put(1)
newQueue.put(2)
newQueue.put(3)
newQueue.put(4)
newQueue.put(5)
print(newQueue.full())
print(newQueue.get())
print(newQueue.get())
print(newQueue.get())
