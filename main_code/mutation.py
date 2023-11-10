from recombination import offspring
import random


def mutation(offspring,length,iterations,n_iteration):
    Basemutationrate = 1
    C = 1000
    Newmutationrate = Basemutationrate /(1 + C*(iterations/n_iteration))
    r1 = random.randint(length)
    offspring.vector[r1] = offspring.vector[r1] + Newmutationrate*random.normal(0,1)
    e= offspring

    return e


