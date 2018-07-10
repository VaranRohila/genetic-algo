from population import *


target = 'Why do you do this to me I am a poor soul'
mr = 0.01
max_pop = 200


pop = population(max_pop,mr,target)


while(not pop.finish):
    print( 'Average_fitness: ' + str(pop.average_fitness()) + '%', 'generation: ' + str(pop.generation))
    pop.generate()
    pop.evaluate()
    i = pop.fitness.index(max(pop.fitness))
    for j in range(len(target)):
        print(pop.species[i].gene[j] , end='')
    print("")
