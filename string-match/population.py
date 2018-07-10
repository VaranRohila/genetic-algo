from dna import *

class population:
    def __init__(self, max_pop, mr, target):
        self.mr = mr
        self.fitness = []
        self.finish = False
        self.target = target
        self.max_pop = max_pop
        self.species = []
        self.generation = 0
        self.max_score = 0
        for i in range(self.max_pop):
            self.species.append(DNA(target))
        for i in range(self.max_pop):
            self.fitness.append(self.species[i].fitness)

    def natural_selection(self):
        i = 0
        while(i < (self.max_pop**2)):
            s1 = random.choice(self.species)
            s2 = random.choice(self.species)
            i += 1
            if s1.fitness > s2.fitness:
                return s1
        return random.choice(self.species)

    def generate(self):
        for i in range(self.max_pop):
            p1 = self.natural_selection()
            p2 = self.natural_selection()
            child = p1.crossover(p2)
            child.mutate(self.mr)
            child.calc_fitness(self.target)
            self.species[i] = child
        self.generation += 1

    def evaluate(self):
        for i in range(self.max_pop):
            self.fitness[i] = self.species[i].fitness
        self.max_score = max(self.fitness)
        if self.max_score == 1:
            self.finish = True

    def average_fitness(self):
        return sum(self.fitness)/self.max_pop
