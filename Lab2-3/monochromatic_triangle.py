class Graph:
    n = 0
    m = 0
    matrix = []
    edges = []

    def __init__(self, filename):
        self.loadData(filename)

    def loadData(self, filename):
        f = open(filename, "r")
        self.n = int(f.readline())
        self.m = int(f.readline())
        self.matrix = [[-1 for _ in range(0, self.n + 1)] for _ in range(0, self.n + 1)]
        for i in range(0, self.m):
            (x, y) = f.readline().split(' ')
            x = int(x)
            y = int(y)
            if x > y:
                aux = x
                x = y
                y = aux
            self.matrix[x][y] = len(self.edges)
            self.matrix[y][x] = len(self.edges)
            self.edges.append((x, y))

    def getN(self):
        return self.n

    def getM(self):
        return self.m

    def getMatrix(self):
        return self.matrix

    def getEdges(self):
        return self.edges

    def numberOfTriangles(self, binaryRepresentation):
        """
        :param binaryRepresentation: the binary representation of the edges
        :return: the number of triangles acording to the graph
        """

        def isInE1(i1, j1):
            if binaryRepresentation[self.matrix[i1][j1]] == 1:
                return True
            return False
        cnt = 0
        for i in range(self.m):
            (x, y) = self.edges[i]
            for z in range(1, self.n + 1):
                if self.matrix[x][z] >= 0 and self.matrix[y][z] >= 0:
                    if isInE1(x, y) == isInE1(x, z) == isInE1(y, z):
                        # print("cycle found: ", x, y, z)
                        cnt += 1
        return cnt // 3
