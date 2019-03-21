from math import sqrt

from State import State
import copy

class Sudoku:
    def __init__(self, fileName):
        self.initialState = State(fileName)

    def __str__(self):
        return str(self.initialState)

    def numberOfZeros(self):
        cnt = 0
        for i in range(0, len(self.initialState.matrix)):
            for j in range(0, len(self.initialState.matrix)):
                if self.initialState.matrix[i][j] == 0:
                    cnt += 1
        return cnt

    def setValue(self, i, j, k):
        self.initialState.matrix[i][j] = k


    def getValue(self, i, j):
        return self.initialState.matrix[i][j]

    def expand(self):
        # returns list of States
        next_states = []
        # i and j go from 0 to n-1
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                # k goes from 1 to n
                for k in range(1, self.initialState.size + 1):
                    root = (int (sqrt (self.initialState.size)))
                    iroot = ( i // root ) * root
                    jroot = ( j// root ) * root
                    if self.initialState.matrix[i][j] == 0 and self.initialState.checkLine(i, k) and self.initialState.checkColumn(j, k) and self.initialState.checkSquare(iroot, jroot, k):
                        next_state = copy.deepcopy(self)
                        next_state.setValue(i, j, k)
                        next_states.append(next_state)
                        # print(next_state)
        return next_states

    def expand_best(self):
        #returns list of States
        best_coefficient = 9
        coefficients = self.heuristic()
        # print(coefficients)
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                if coefficients[i][j] < best_coefficient and self.initialState.matrix[i][j] == 0:
                    best_coefficient = coefficients[i][j]
        next_states = []
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                for k in range(1, self.initialState.size + 1):
                    root = (int(sqrt(self.initialState.size)))
                    iroot = (i // root) * root
                    jroot = (j // root) * root
                    if self.initialState.matrix[i][j] == 0 and self.initialState.checkLine(i, k) and self.initialState.checkSquare(iroot, jroot, k) and self.initialState.checkColumn(j, k):
                        # print(self.initialState)
                        if coefficients[i][j] == best_coefficient:
                            new_state = copy.deepcopy(self)
                            new_state.setValue(i, j, k)
                            next_states.append(new_state)
        return next_states

    def completed(self):
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                if self.initialState.matrix[i][j] == 0:
                    return False
        return True

    def heuristic(self):
        #makes the matrix of coefficients
        coefficients = [[0 for _ in range(self.initialState.size)] for _ in range(self.initialState.size)]
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                if self.initialState.matrix[i][j] == 0:
                    for k in range(1, self.initialState.size + 1):
                        root = (int(sqrt(self.initialState.size)))
                        iroot = (i // root) * root
                        jroot = (j // root) * root
                        if self.initialState.matrix[i][j] == 0 and self.initialState.checkColumn(j, k) and self.initialState.checkLine(i, k) and self.initialState.checkSquare(iroot, jroot, k):
                            coefficients[i][j] += 1
        return coefficients

    def __eq__(self, other):
        for i in range(self.initialState.size):
            for j in range(self.initialState.size):
                if self.initialState.matrix[i][j] != other.getValue(i, j):
                    return False
        return True


