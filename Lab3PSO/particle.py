import random


class Particle:
    def __init__(self, problem):
        self.problem = problem
        self.position = [random.randint(0, 1) for _ in range(self.problem.n)]
        self.velocity = [0 for _ in
                         range(self.problem.n)]  # the probability of making the particle look like the best one
        self.bestPosition = self.position
        self.fitness = self.fitnessFunction()
        self.bestFitness = self.fitness

    @staticmethod
    def is_in(l1, l2):  # only for sets
        cnt = 0
        for i in l1:
            if i in l2:
                cnt += 1
        return cnt == len(l1)

    def fitnessFunction(self):
        cnt = 0
        aux1 = []
        for i in range(len(self.position)):
            if self.position[i] == 1:
                aux1.append(self.problem.A[i])
        aux2 = []
        for i in range(len(self.position)):
            if self.position[i] == 0:
                aux2.append(self.problem.A[i])
        for s in self.problem.S:
            if (not self.is_in(s, aux1)) and (not self.is_in(s, aux2)):
                cnt += 1
        return cnt

    def evaluate(self):
        # is the value better or worse than i already have
        if self.bestFitness > self.fitnessFunction():
            return True
        return False

    def update(self, particle):
        # if the value is better, update the memory
        print("old position: ", self.position, "old finess: ", self.fitness)
        self.position = particle.position.copy()
        self.fitness = self.fitnessFunction()
        print("new position: ", self.position, "new fitness: ", particle.fitness)
        if particle.fitness > self.bestFitness:
            self.bestPosition = particle.position
            self.bestFitness = particle.fitness
        print("best fitness: ", self.bestFitness, "best postition:", self.bestPosition)

    def __str__(self):
        return str(self.position) + " " +str(self.fitness)
