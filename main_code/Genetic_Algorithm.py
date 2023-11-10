import random
from Fitness import fitnessFunc, generate_random_vector
from roulette_wheel_selection import roulette_wheel_selection
from initpopulation import n_iteration, population, n_population, length
from recombination import recombination
from mutation import mutation
from survival import survival


for iterations in [1,n_iteration]:
    p1 = roulette_wheel_selection(population, n_population)
    p2 = roulette_wheel_selection(population, n_population)
    offspring = recombination(p1,p2,length)
    offspring = mutation(offspring, length, iterations, n_iteration)
    offspring.fitness = fitnessFunc(offspring, population.ch.vector)
    population = survival(population, offspring, n_population)
    if (iterations % 10000) == 0:
        iterations




 
    











