import random
import numpy

from individ import Individ


class Population:

    def __init__(self, noOfIndivids, list):
        self.noOfIndivids = noOfIndivids
        self.listOfIndivids = list

    def getIndivids(self):
        return self.listOfIndivids

    def selection(self, size):
        '''

        :return:
        '''

        fitness = []
        for i in self.listOfIndivids:
            fitness.append(i.fitness())
        fitnessSum = sum(fitness)
        normalized_fitness = [f / fitnessSum for f in fitness]
        return numpy.random.choice(self.listOfIndivids, size, p=normalized_fitness, replace=False).tolist()

    def evaluate(self):
        result = 0
        for i in self.listOfIndivids:
            if i.fitness() > result:
                result = i.fitness()
        return result

    def best(self):
        # returns best individ
        bestCoefficient = self.evaluate()
        for i in self.listOfIndivids:
            if i.fitness() == bestCoefficient:
                return i
        return None
