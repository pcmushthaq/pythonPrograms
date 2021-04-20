# Python Implementation of LinkedList

# Node Class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node: Node):
        self.head = node
        self.tail = node
        self.length = 1

    # print the linkedList
    def printList(self):
        array = []
        currentNode = self.head
        while(currentNode is not None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)

    # Traverse to index
    def traverseToIndex(self, index: int) -> Node:
        currentNode = self.head
        counter = 0
        while(counter != index):
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def append(self, node: Node):
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, node: Node):
        node.next = self.head
        self.head = node
        self.length += 1

    def insertAtIndex(self, index: int, node: Node):
        if(index == 0):
            self.prepend(node)
        elif (index == self.length):
            self.append(node)
        else:
            leader = self.traverseToIndex(index-1)
            follower = leader.next
            leader.next = node
            node.next = follower
            self.length += 1

    def remove(self, index: int):
        if(index >= self.length):
            return
        leader = self.traverseToIndex(index-1)
        toBeRemoved = leader.next
        leader.next = toBeRemoved.next
        del toBeRemoved
        self.length -= 1


linkedList = LinkedList(Node(1))
linkedList.printList()
linkedList.append(Node(10))
linkedList.printList()
linkedList.insertAtIndex(1, Node(5))
linkedList.printList()
linkedList.insertAtIndex(1, Node(2))
linkedList.printList()
linkedList.remove(2)
linkedList.printList()
