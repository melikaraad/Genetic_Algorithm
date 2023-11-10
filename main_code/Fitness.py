from math import exp
import random

def fitnessFunc(a):
    mysum = 0
    mystep = 0.1
    for i in [1,10]:
        mysum = mysum + abs(-0.5*a[0]*exp(mystep*i) + 0.5*a[0]*exp(mystep*i) + 0.5*a[1] + 0.25)
    
    mysum = mysum + 10*abs(0.5*a[1] + 0.25)
    eps = 2.220446049250313*exp(-16)
    fitness = 1/(mysum + eps)
    return fitness

def generate_random_vector(length):
    random_vector = [random.random() for _ in range(length)]
    return random_vector


