from initpopulation import population, n_population
import random

def roulette_wheel_selection(population, n_population):

    population_fitness = sum(m['fitness'] for m in population)

    i=0
    r = random.random()*population_fitness
    temp = population[1]['fitness']
    while r > temp:
        i= i + 1
        temp = temp + population[1]['fitness']
        if i >= n_population:
            break
    m = population[i]

    return m

p = population
n = n_population

S = roulette_wheel_selection(p, n)
print(S)

