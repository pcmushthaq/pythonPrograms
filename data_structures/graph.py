class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, value):
        self.adjacentList[value] = []
        self.numberOfNodes += 1

    def addEdges(self, node1, node2):
        if(node1 not in self.adjacentList or node2 not in self.adjacentList):
            return
        self.adjacentList[node2].append(node1)
        self.adjacentList[node1].append(node2)

    def showConnections(self):
        for key, value in self.adjacentList.items():
            print(str(key)+'-->'+str(value))


# https://visualgo.net/en/graphds
# We are trying to create this DAG

graph = Graph()
graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addEdges(3, 1)
graph.addEdges(3, 4)
graph.addEdges(4, 2)
graph.addEdges(4, 5)
graph.addEdges(1, 2)
graph.addEdges(1, 0)
graph.addEdges(0, 2)
graph.addEdges(6, 5)
graph.showConnections()
