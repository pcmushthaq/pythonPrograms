# Python Implementation of LinkedList

# Node Class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1

    def pop(self):
        toBeRemoved = self.tail
        secondLast = toBeRemoved.prev
        secondLast.next = None
        del toBeRemoved
        self.length -= 1

    def prepend(self, node: Node):
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1

    def insertAtIndex(self, index: int, node: Node):
        if(index == 0):
            self.prepend(node)
        elif (index == self.length):
            self.append(node)
        else:
            # if we are insering 1 in betweem 2 and 3
            # Then 2 is the leader and 3 is the foloower
            leader = self.traverseToIndex(index-1)
            follower = leader.next
            follower.prev = node
            leader.next = node
            node.next = follower
            node.prev = leader
            self.length += 1

    def remove(self, index: int):
        if(index >= self.length):
            return
        leader = self.traverseToIndex(index-1)
        toBeRemoved = leader.next
        follower = toBeRemoved.next
        leader.next = follower
        follower.prev = leader
        del toBeRemoved
        self.length -= 1


linkedList = DoublyLinkedList(Node(1))
linkedList.printList()
linkedList.append(Node(10))
linkedList.printList()
linkedList.insertAtIndex(1, Node(5))
linkedList.printList()
linkedList.insertAtIndex(1, Node(2))
linkedList.printList()
linkedList.remove(2)
linkedList.printList()
linkedList.insertAtIndex(1, Node(15))
linkedList.printList()
linkedList.insertAtIndex(1, Node(18))
linkedList.printList()
linkedList.pop()
linkedList.printList()
