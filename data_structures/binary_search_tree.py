import json


class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def lookup(self, value):
        currentNode = self.root
        while True:
            if(value == currentNode.value):
                return currentNode

            elif(currentNode.right is None and currentNode.left is None):
                return 'NOT FOUND'
            elif(value < currentNode.value and currentNode.left is not None):
                currentNode = currentNode.left

            elif (value < currentNode.value and currentNode.left is None):
                return 'NOT FOUND'

            elif(value > currentNode.value and currentNode.right is not None):
                currentNode = currentNode.right

            elif (value > currentNode.value and currentNode.right is None):
                return "NOT FOUND"

    def insert(self, node: Node):
        if(self.root is None):
            self.root = node
            return
        lastNode = self.traverse(node.value)
        if(lastNode.value < node.value):
            lastNode.right = node
        elif(node.value < lastNode.value):
            lastNode.left = node

    def traverse(self, value) -> Node:
        currentNode = self.root
        while True:
            if(value < currentNode.value and currentNode.left is not None):
                currentNode = currentNode.left

            elif (value < currentNode.value and currentNode.left is None):
                return currentNode

            elif(value > currentNode.value and currentNode.right is not None):
                currentNode = currentNode.right

            elif (value > currentNode.value and currentNode.right is None):
                return currentNode


def traverse(node: Node):
    tree = {'value': node.value}
    tree['left'] = traverse(node.left) if node.left is not None else None
    tree['right'] = traverse(node.right) if node.right is not None else None
    return tree


bst = BinarySearchTree()
bst.insert(Node(5))
bst.insert(Node(2))
bst.insert(Node(4))
bst.insert(Node(3))
print(json.dumps(traverse(bst.root)))
print(bst.lookup(3))
print(bst.lookup(6))
print(bst.lookup(1))
