import math
from random import random


class Controller:
    def __init__(self, swarm, noIterations):
        self.population = swarm
        self.noIterations = noIterations
        self.w = 1.0
        self.c1 = 1.
        self.c2 = 2.5


    def iteration(self):
        """
        for each particle, update the velocity and the position
        according to the particle's memory and the best particle's position
        :return:
        """
        bestParticles = self.population.getBestParticles()
        for i in range(self.population.numberOfParticles):
            for j in range(len(self.population.listOfParticles[0].velocity)): #size of the velocity
                newVelocity = self.w * self.population.listOfParticles[i].velocity[j]
                newVelocity = newVelocity + self.c1 * random() * (bestParticles[i].position[j] - self.population.listOfParticles[i].position[j])
                newVelocity = newVelocity + self.c2 * random() * (self.population.listOfParticles[i].bestPosition[j] - self.population.listOfParticles[i].position[j])
                self.population.listOfParticles[i].velocity[j] = newVelocity

        for i in range(len(self.population.listOfParticles)):
            # print(self.population.listOfParticles[i].velocity)
            newPosition = []
            for j in range(len(self.population.listOfParticles[0].velocity)):
                s = 1 / (1 + math.exp(-self.population.listOfParticles[i].velocity[j]))
                rand = random()
                if rand <= s:
                    # print(, "list of part")
                    newPosition.append(self.population.listOfParticles[i].position[j])
                else:
                    newPosition.append(bestParticles[i].position[j])
            self.population.listOfParticles[i].position = newPosition
        return self.population.listOfParticles

    def runAlg(self):
        for i in range(self.noIterations):
            self.iteration()
            if self.checkSolution():
                return self.checkSolution()
        bestOne = self.population.getBestParticles()[0]
        for i in self.population.getBestParticles():
            if i.fitness > bestOne.fitness:
                bestOne = i
        print("aici")
        return bestOne

    def checkSolution(self):
        """
        checks if a solution is found
        fitness == number of subsets
        :return: solution, else False
        """

        for i in self.population.listOfParticles:

            if i.fitness == i.problem.m:
                return i
        return False