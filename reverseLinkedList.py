from linkedList import LinkedList, Node


def reverseLList(linkedList: LinkedList):
    # Better solution
    # Single Loop, Reverse pointers and replace head and tail
    head = linkedList.head

    # This step is also crucial
    linkedList.tail = head
    first = head
    second = head.next
    while(second is not None):
        temp = second.next
        # This is the key point
        # We are just reversing the pointers
        second.next = first
        # These are only for continuing the loop
        first = second
        second = temp
    linkedList.head.next = None
    linkedList.head = first


def reverseLinkedList(linkedList: LinkedList):
    # Brute Force Solution
    currentNode = linkedList.head
    values = []

    while currentNode is not None:
        values.append(currentNode.value)
        currentNode = currentNode.next
    for i in range(linkedList.length):
        node = linkedList.traverseToIndex(i)
        node.value = values[linkedList.length-1-i]
    # This is an O(n+n) solution?


linkedList = LinkedList(Node(1))
testList = [2, 3, 4, 5, 6, 7, 8, 9]
for num in testList:
    linkedList.append(Node(num))
linkedList.printList()
# Reverse using better solution
reverseLList(linkedList)
linkedList.printList()
# BruteForce Solution
reverseLinkedList(linkedList)
linkedList.printList()
