import random
from math import sqrt


def mean(data):
    return float(sum(data)) / len(data)


def variance(data):
    mu = mean(data)
    return sum([(x - mu) ** 2 for x in data]) / len(data)


def stddev(data):
    return sqrt(variance(data))


def flip(N):
    # Insert your code here
    return [ random.random() > 0.5 for x in range(N) ]

def sample(N):
    #Insert your code here
    return [ mean(flip(N)) for i in range(N) ]

N = 1000
f = flip(N)

outcomes=sample(N)

import matplotlib.pyplot as plt

plt.hist(outcomes,bins=30)
plt.show()

