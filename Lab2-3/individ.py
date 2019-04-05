from random import *

from monochromatic_triangle import Graph


class Individ:
    def __init__(self, graph):
        """
        representation: binary array, possible configuration
        :param size: the size of the array
        """
        self.graph = graph
        self.size = graph.getM()
        self.array = [randint(0, 1) for _ in range(self.size)]

    def fitness(self):
        """
            computes fitness function
            1 / (1 + number of cycles)
            returns float
        """
        # print("fitness:", 1 / (1 + Graph.numberOfTriangles(self.graph, self.array)), self.array)
        return 1 / (1 + Graph.numberOfTriangles(self.graph, self.array))

    def mutate(self, probability):
        """
        computes mutation
        flip a bit according to probability
        :return:
        """

        if probability < 0.05:
            position = randint(0, self.size-1)
            print(position)
            if self.array[position] == 0:
                self.array[position] = 1
            else:
                self.array[position] = 0

    def crossover(self, individ2):
        """
        computes crossover -> bit representation
        :param individ1:
        :param probability:
        :return:
        """
        probability = 0.5
        size = self.size
        offspring1 = Individ(self.graph)
        offspring2 = Individ(self.graph)
        cutPoint = size * probability
        for i in range(0, size):
            if i < cutPoint:
                offspring1.array[i] = self.array[i]
                offspring2.array[i] = individ2.array[i]
            else:
                offspring2.array[i] = self.array[i]
                offspring1.array[i] = individ2.array[i]
        return offspring1, offspring2
