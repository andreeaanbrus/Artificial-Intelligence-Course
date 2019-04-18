import random


class Swarm:
    def __init__(self, numberOfParticles, listOfParticles, noNeighbours):
        self.numberOfParticles = numberOfParticles
        self.listOfParticles = listOfParticles
        self.numberOfNeighbours = noNeighbours
        self.neighbours = dict()
        self.makeNeighbours()

    def makeNeighbours(self):
        """
        for each particle choose numberOfNeighbours random particles to be its neighbours form listOfParticles
        :return:
        """
        for particle in self.listOfParticles:
            copyList = self.listOfParticles.copy()
            copyList.remove(particle)
            self.neighbours.update({particle: random.sample(self.listOfParticles, self.numberOfNeighbours)})

    def getBestNeighbour(self, particle):
        """
        :param particle:
        :return: detemrine the best neighbour for the given particle
        """
        for neighbour in self.neighbours.get(particle):
            # print("neighbour:", str(neighbour))
            if neighbour.fitness > particle.fitness:
                return neighbour
        return particle

    def getBestParticles(self):
        bestParticles = []
        for particle in self.listOfParticles:
            bestParticles.append(self.getBestNeighbour(particle))
        return bestParticles
