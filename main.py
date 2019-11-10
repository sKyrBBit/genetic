import random
import matplotlib.pyplot as mp


def mp_initialize():
    mp.xlim(1, 8192)
    mp.ylim(1, 8192)
    mp.xscale('log')
    mp.yscale('log')


class Gene:
    x = 0
    y = 0
    fitness = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fitness = distance(x, y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


# distance from (1, 1)
def distance(x, y):
    p = x - 1
    q = y - 1
    return p * p + q * q


def generate():
    global genes
    generation = 0
    while True:
        generation += 1
        saved = save()      # save the best gene
        if saved.x == 1 and saved.y == 1:
            return saved
        tmp = [saved]
        for j in range(1):  # mutate
            tmp.append(mutate())
        a = best()
        genes.remove(a)
        b = best()
        genes.remove(b)
        for j in range(4):  # cross dominant gene
            tmp.append(cross(a, b))
        a = best()
        genes.remove(a)
        b = best()
        genes.remove(b)
        for j in range(2):  # cross recessive gene
            tmp.append(cross(a, b))
        genes = tmp
        mp.title("generation={0}".format(generation))
        mp_initialize()
        mp.plot(list(map(lambda g: g.x, genes)), list(map(lambda g: g.y, genes)),
                color='red', marker='x', markersize=15, linestyle='None')
        mp.show()


def best():
    f = map(lambda gene: gene.fitness, genes)
    m = min(f)
    return list(filter(lambda gene: gene.fitness == m, genes))[0]


def save():
    t = best()
    genes.remove(t)
    return t


def mutate():
    tmp = genes[random.randrange(0, genes.__len__())]
    genes.remove(tmp)
    m = random.randrange(0, 1)
    if m == 0:
        return Gene(tmp.x//2, tmp.y//2)
    else:
        return Gene(tmp.x*2, tmp.y*2)


def cross(a, b):
    m = random.randrange(0, 7)
    if m == 0:
        return Gene(a.x, b.x)
    elif m == 1:
        return Gene(a.x, b.y)
    elif m == 2:
        return Gene(a.y, b.x)
    elif m == 3:
        return Gene(a.y, b.y)
    elif m == 4:
        return Gene(b.x, a.x)
    elif m == 5:
        return Gene(b.x, a.y)
    elif m == 6:
        return Gene(b.y, a.x)
    else:
        return Gene(b.y, a.y)


genes = []
for i in range(8):
    genes.append(Gene(random.randrange(1, 8192), random.randrange(1, 8192)))
mp.title("generation=0")
mp_initialize()
mp.plot(list(map(lambda g: g.x, genes)), list(map(lambda g: g.y, genes)),
        color='red', marker='x', markersize=15, linestyle='None')
mp.show()
print("answer is {0}".format(generate()))
