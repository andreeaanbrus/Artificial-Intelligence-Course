import numpy
import matplotlib.pyplot as plt


class Algorithm:
    population = []

    def __init__(self, graph, population, probability, iterations):
        self.graph = graph
        self.population = population
        self.probability = probability
        self.iterations = iterations

    def iteration(self):
        selection = self.population.selection(self.population.noOfIndivids)
        parent1 = numpy.random.permutation(self.population.noOfIndivids)
        parent2 = numpy.random.permutation(self.population.noOfIndivids)
        children = []
        for i in range(len(parent1)):
            (child1, child2) = selection[parent1[i]].crossover(selection[parent2[i]])
            child1.mutate(self.probability)
            children.append(child1)
            children.append(child2)
        for c in children:
            self.population.listOfIndivids.append(c)

    def run(self):
        fitness_history = []
        while self.iterations != 0:
            self.iteration()
            self.iterations -= 1
            for i in self.population.selection(self.population.noOfIndivids):
                print(i.array)
                fitness_history.append(i.fitness())
                if i.fitness() == 1:
                    plt.plot(fitness_history)
                    plt.ylabel('Fitness history')
                    plt.show()
                    return i
        plt.plot(fitness_history)
        plt.ylabel('Fitness history')
        plt.show()
        return None
