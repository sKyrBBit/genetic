import random as r
import numpy.random as nr


def random_point():
    return r.randrange(-256, 255), r.randrange(-256, 255)


def random_gene():
    return [r.randrange(0, 5 - i) for i in range(5)]


def distance(a: (int, int), b: (int, int)):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x * x + y * y


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
        ps = map(lambda p: round(p, 3), ps)
        ps = list(ps).append(1 - sum(ps))
        n = Gene()
        g.append(n)
        c = nr.choice(6, 1, p=ps)[0]
        if not(c is n):
            return g[c]


def generate():
    g = genes.copy()
    m1 = g[r.randrange(0, 7)]
    g.remove(m1)
    m2 = g[r.randrange(0, 6)]
    g.remove(m2)
    s = [mutate(m1), mutate(m2)]
    for i in range(3):
        s.extend(cross(select(g), select(g)))
    return s


A = random_point()
B = random_point()
C = random_point()
D = random_point()
E = random_point()
cities = [A, B, C, D, E]
print("A: {0}\nB: {1}\nC: {2}\nD: {3}\nE: {4}\n".format(A, B, C, D, E))
genes = [Gene() for i in range(8)]
for i in range(200):
    print("genes?max={0}: [".format(max(map(lambda g: g.fitness, genes))))
    for g in genes:
        g.print()
    print("]")
    genes = generate()
