import random


class Animal:
    def __init__(self, genotype):
        self.genotype = genotype

    genotype = []
    fit = 0


def initial():
    animals = []
    for i in range(50):
        temp = []
        for j in range(8):
            temp.append(random.randint(0, 7))
        animals.append(Animal(list(temp)))
    return animals


def fitness(anim):
    errors = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if anim.genotype[i] == anim.genotype[j]:
                errors += 1
            if anim.genotype[i] + (j - i) == anim.genotype[j]:
                errors += 1
            if anim.genotype[i] - (j - i) == anim.genotype[j]:
                errors += 1
    fitfinal = 28 - errors
    anim.fit = fitfinal


def selection(animals):
    sum = 0
    chanses = []
    selected = []
    for animal in animals:
        sum += animal.fit
    chanses.append(animals[0].fit / sum)
    for i in range(1, 50):
        chanses.append(animal.fit / sum + chanses[i - 1])
    for i in range(50):
        randomnumber = round(random.uniform(0, 1), 3)
        for j in range(50):
            if chanses[j] >= randomnumber:
                if j == 0:
                    selected.append(animals[j])
                else:
                    selected.append(animals[j - 1])
                break
    return random.shuffle(selected)


def crossover(selected):
    childs = []
    for i in range(0, 50, 2):
        split = random.randint(1, 6)
        genotype1 = selected[i].genotype[0:split]
        genotype1.append(selected[i + 1].genotype[split + 1:7])
        genotype2 = selected[i + 1].genotype[0:split]
        genotype2.append(selected[i].genotype[split + 1:7])
        childs.append(Animal(genotype1))
        childs.append(Animal(genotype2))
    return childs


def Mutation(childs):
    for i in range(2):
        select = random.randint(0, 49)
        childs[select].genotype[random.randint(0, 7)] = random.randint(0, 7)


def stop_condition(parents):
    for parent in parents:
        if parent.fit == 28:
            return False
    return True


def maingenetic():
    parents = initial()
    for i in range(50):
        fitness(parents[i])
    while stop_condition(parents):
        selected = selection(parents)
        childs = crossover(selected)
        Mutation(childs)
        for i in range(50):
            fitness(childs)
        parents = childs


maingenetic()
