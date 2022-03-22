# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Graph():
    ### ASSUMES SEQUENTIAL INTEGER VALUES FOR VERTICES
    def __init__(self):
        self.edges = {}
        self.vertices = []


    # for printing the Graph vertexes
    def generate_edges(self):
        for i in self.edges.keys():
            print(i,' -> ', ' , '.join([str(j) for j in self.edges[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertices have been seen before
        if fromVertex not in self.vertices:
            self.vertices.append(fromVertex)
        if toVertex not in self.vertices:
            self.vertices.append(toVertex)

        # check if vertex is already present,
        if fromVertex in self.edges.keys():
            self.edges[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.edges[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        # Take a list for stoting already visited vertexes
        visited = [False] * len(self.edges)

        # create a list to store all the vertexes for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            startVertex = queue.pop(0)
            print(startVertex, end = ' ')

            # mark all adjacent nodes as visited and print them
            for i in self.edges[startVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self):
        # visited array for storing already visited nodes
        visited = [False] * len(self.edges)

        # call the recursive helper function
        for i in range(len(self.edges)):
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end=' ')

        # Recur for all the vertexes that are adjacent to this node
        for i in self.edges.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)

    def isConnected(self, start, dest):
        # Mark all the vertices as not visited
        print(self.vertices)
        visited = [False] * (len(self.vertices))

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(start)
        visited[start] = True

        while queue:

            # Dequeue a vertex from queue
            n = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if n == dest:
                return True

            #  Else, try to continue to do BFS
            #  If we are unable, it means no edges exist from the node
            try:
                for i in self.edges[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            except:
                if len(queue) == 0:
                    return False

        # If BFS is complete without visited dest
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = Graph()
    g.addEdge(1,3)
    g.addEdge(1,2)
    g.generate_edges()
    print(g.isConnected(2, 3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
