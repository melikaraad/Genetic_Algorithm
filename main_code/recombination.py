#ravesh tarkib = tarkib baznamyi aadad haghighi
import random
from roulette_wheel_selection import S
from initpopulation import length
from Fitness import fitnessFunc


def recombination (p1,p2,length):
    v=[]
    for i in [0,length-1]:
        r = random.random()
        v[i] = p1['vector'][i]*r + (1-r)*p2['vector'][i]
        v.append(v[i])
        fitness  = fitnessFunc(v)

    offspring = {'vector': v, 'fitness': fitness}

    return offspring

offspring  = recombination(S['vector'][0], S['vector'][1],length)




