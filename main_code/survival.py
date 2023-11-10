from initpopulation import n_population, population
from recombination import offspring

def survival(population,offspring,n_population):
    mymin = float('inf')
    index = 0
    for i in [0,n_population - 1]:
        if population[i].fitness < mymin:
            index = i
            mymin = population[i].fitness
    
    population[index] = offspring
    e=population

    return e
