import string
import random
import math
# Funtion to calculate fitness
def calc_fitness(s, target):
    s.fitness = 0
    for i in range(s.l):
        if s.gene[i] == target[i]:
            s.fitness += 1
    s.fitness /= s.l
class DNA:
    fitness = 0
    # Initialize with random genes
    def __init__(self, target):
        self.gene = []
        self.l = len(target)
        self.target = target
        for i in range(self.l):
            self.gene.append(random.choice(string.ascii_letters + ' '))
        calc_fitness(self,target)

    def crossover(self, partner):
        child = DNA(self.target)
        point = random.randrange(self.l)
        for i in range(self.l):
            if i < point:
                child.gene[i] = self.gene[i]
            else:
                child.gene[i] = partner.gene[i]
        return child

    def calc_fitness(self, target):
        self.fitness = 0
        for i in range(self.l):
            if self.gene[i] == target[i]:
                self.fitness += 1
        self.fitness /= self.l


    def mutate(self, mr):
        for i in range(self.l):
            chance = random.random() < mr
            if chance:
                self.gene[i] = random.choice(string.ascii_letters + ' ')
