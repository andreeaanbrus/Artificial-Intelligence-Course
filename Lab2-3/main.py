from algorithm import Algorithm
from individ import Individ
from monochromatic_triangle import Graph
from population import Population


def main():
    g = Graph(filename="graph.txt")
    individ = Individ(g)
    individ2 = Individ(g)
    individ3 = Individ(g)
    individ4 = Individ(g)
    individ5 = Individ(g)
    individ6 = Individ(g)
    individ7 = Individ(g)
    individ8 = Individ(g)
    individ9 = Individ(g)
    p = Population(9, [individ, individ2, individ3, individ4, individ5, individ6, individ7, individ8, individ9])
    a = Algorithm(g, p, 0.03, 100)
    a.run()

main()