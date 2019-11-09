import random


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


# distance from (0, 0)
def distance(x, y):
    return x * x + y * y


def generate():
    global genes
    while True:
        saved = save()      # save the best gene
        if saved.x == 0 and saved.y == 0:
            return saved
        tmp = [saved]
        for j in range(3):  # mutate
            tmp.append(mutate())
        a = best()
        genes.remove(a)
        b = best()
        genes.remove(b)
        for j in range(3):  # cross dominant gene
            tmp.append(cross(a, b))
        a = best()
        genes.remove(a)
        b = best()
        genes.remove(b)
        for j in range(1):  # cross recessive gene
            tmp.append(cross(a, b))
        genes = tmp
        for gene in genes:
            print(gene.__str__(), end=", ")
        print("\b\b")


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
    genes.append(Gene(random.randrange(0, 255), random.randrange(0, 255)))
print("answer is {0}".format(generate()))
