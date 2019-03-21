from math import sqrt


class State:
    def __init__(self, fileName):
        self.fileName = fileName
        self.matrix = []
        self.size = 0
        self.readFromFile()

    def readFromFile(self):
        with open(self.fileName, 'r') as f:
            self.size = int(f.readline())
            self.matrix = [[] for _ in range(self.size)]
            k = 0
            for line in f:
                self.matrix[k] = line.split()
                k += 1
            for i in range(0, k):
                for j in range(k):
                    self.matrix[i][j] = int(self.matrix[i][j])

    def __eq__(self, other):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != other.get_value(i, j):
                    return False
        return True

    def __str__(self):
        string_builder = ""
        for i in self.matrix:
            for j in i:
                string_builder += str(j)
                string_builder += ' '
            string_builder += '\n'
        return string_builder

    def checkLine(self, i, k):
#         check if k can be put on line i
        for j in range(self.size):
            if k == self.matrix[i][j]:
                return False
        return True

    def checkColumn(self, j, k):
#         check if k can be put on column j
        for i in range(self.size):
            if k == self.matrix[i][j]:
                return False
        return True

    def checkSquare(self, iroot, jroot, k):
        for i in range(iroot, iroot + int(sqrt(self.size))):
            for j in range(jroot, jroot + int(sqrt(self.size))):
                if  k == self.matrix[i][j]:
                    return False
        return True

