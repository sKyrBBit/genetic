import random as r
import numpy.random as nr
import numpy as n


def random_point():
    return r.randrange(-256, 255), r.randrange(-256, 255)


def random_gene():
    return [r.randrange(0, 5 - i) for i in range(5)]


def distance(a: (float, float), b: (float, float)):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return n.sqrt(x * x + y * y)


def fitness(gene: list):
    current = None
    f = 0
    c = cities.copy()
    for g in gene:
        if not (current is None):
            f += distance(current, c[g])
        current = c[g]
        c.remove(current)
    return 1 / f


class Gene:
    gene = []
    fitness = 0

    def __init__(self, gene=None):
        if gene is None:
            gene = random_gene()
        self.gene = gene
        self.fitness = fitness(gene)

    def print(self):
        print("\tgene={0} fitness={1},".format(self.gene, self.fitness))


def probability(a: Gene):
    return a.fitness / sum(map(lambda g: g.fitness, genes))


def save(a: Gene):
    return Gene(a.gene.copy())


def mutate(a: Gene):
    b = a.gene.copy()
    b[0] = r.randrange(0, 4)  # mutate elements at 0
    return Gene(b)


def cross(a: Gene, b: Gene):
    c = a.gene.copy()
    d = b.gene.copy()
    for i in range(r.randrange(0, 4), 4):  # swap elements at 'r.randrange(0, 4), 4' and after
        e = d[i]
        d[i] = c[i]
        c[i] = e
    return Gene(c), Gene(d)


def select(g: list):
    while True:
        ps = map(probability, g)
        ps = map(lambda p: round(p, 8), ps)
        ps = list(ps).append(1 - sum(ps))
        n = Gene()
        g.append(n)
        c = nr.choice(52, 1, p=ps)[0]
        if not(c is n):
            return g[c]


def generate():
    g = genes.copy()
    n = []
    for i in range(2):  # save
        t = select(g)
        g.remove(t)
        n.append(save(t))
    for i in range(2):  # mutate
        t = g[r.randrange(0, 59 - i)]
        g.remove(t)
        n.append(mutate(t))
    for i in range(30):  # cross
        n.extend(cross(select(g), select(g)))
    return n


A = (1.000, 0.000)
B = (0.309, 0.951)
C = (-0.809, 0.588)
D = (-0.809, -0.588)
E = (0.309, -0.951)
cities = [A, B, C, D, E]
print("A: {0}\nB: {1}\nC: {2}\nD: {3}\nE: {4}\n".format(A, B, C, D, E))
genes = [Gene() for i in range(64)]
for i in range(256):
    print("genes?max={0}: [".format(max(map(lambda g: g.fitness, genes))))
    for g in genes:
        g.print()
    print("]")
    genes = generate()
