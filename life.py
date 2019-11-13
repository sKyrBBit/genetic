import sys
import random as r
import numpy.random as nr
import numpy as np
from matplotlib import pyplot
from matplotlib import patches


def random_forest():
    return (r.randrange(-512, 511), r.randrange(-512, 511)), r.randrange(1, 64)


def random_gene():
    return [r.randrange(0, 5) for i in range(5)]


class Life:
    location = ()
    gene = []

    def __init__(self, gene=None):
        if gene is None:
            gene = random_gene()
        self.gene = gene


def fitness(a: Life):
    return 100


def probability(a: Life):
    return fitness(a) / sum(map(fitness, lives))


def save(a: Life):
    a_ = a.gene.copy()
    # save
    return Life(a_)


def mutate(a: Life):
    a_ = a.gene.copy()
    # mutate
    return Life(a_)


def cross(a: Life, b: Life):
    a_ = a.gene.copy()
    b_ = b.gene.copy()
    for i in range(r.randrange(0, 4), 4):  # swap elements at 'r.randrange(0, 4)' and after
        tmp = b_[i]
        b_[i] = a_[i]
        a_[i] = tmp
    return Life(a_), Life(b_)


def select(l: list):
    while True:
        ps = map(probability, l)
        ps = map(lambda p: round(p, 8), ps)
        ps = list(ps).append(1 - sum(ps))
        t = Life()
        l.append(t)
        c = nr.choice(52, 1, p=ps)[0]
        if not(c is t):
            return l[c]


def generate():
    print("generate")


# plane = [-512, 511] * [-512, 511]
# gene = [oxygen, water, nutrition, space, light]
lives = []
forests = []
if __name__ == '__main__':
    # lives = 1024
    lives = [Life() for i in range(1024)]
    # forests = 8
    forests = [random_forest() for i in range(8)]
    pyplot.figure(figsize=(8, 8))
    pyplot.xlim(-512, 511)
    pyplot.ylim(-512, 511)
    ax = pyplot.axes()
    for f in forests:
        c = patches.Circle(xy=f[0], radius=f[1], fc="lime", ec="mediumspringgreen")
        ax.add_patch(c)
    pyplot.axis('scaled')
    ax.set_aspect('equal')
    pyplot.show()
    sys.exit(0)
    # generations = 128
    for i in range(128):
        pyplot.title("generation={0}".format(i))
        lives = generate()
