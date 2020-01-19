import random
import operator
import numpy
import math

prep = 5
CityCount = 200
baseList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
CityList = []

x = [14, 31, 61, 16, 33, 3, 50, 95, 12, 53, 89, 56, 70, 31, 72, 33, 54, 20, 80, 80]
y = [96, 93, 45, 18, 68, 2, 96, 58, 20, 38, 71, 34, 7, 57, 32, 45, 16, 68, 26, 28]


def make_city_list(city_list, x, y):
    for i in range(len(x)):
        city_list.append(City(x[i], y[i]))


class City:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class CitySet:
    def __init__(self, genotype):
        self.genotype = genotype

    genotype = []
    fit = 0


def initial():
    result = []
    for i in range(CityCount):
        random.shuffle(baseList)
        result.append(CitySet(list(baseList)))
    return result


def distance(A, B):
    return math.sqrt(pow(A.x - B.x, 2) + pow(A.y - B.y, 2))


def fitness(set):
    cost = 0
    for i in range(20):
        if i != 19:
            c1index = set.genotype[i]
            c2index = set.genotype[i + 1]
        else:
            c1index = 19
            c2index = 0
        c1 = CityList[c1index]
        c2 = CityList[c2index]
        costc12 = costc12 + distance(c1, c2)
    set.fit = 1 / cost


def selection(animals):
    sum = 0
    chanses = []
    selected = []
    for animal in animals:
        sum += animal.fit
    chanses.append(round(animals[0].fit / sum, 4))
    for i in range(1, 50):
        chanses.append(round(animal.fit / sum + chanses[i - 1], 4))
    for i in range(50):
        randomnumber = round(random.uniform(0, 1), 5)
        for j in range(50):
            if chanses[j] >= randomnumber:
                if j == 0:
                    selected.append(animals[j])
                else:
                    selected.append(animals[j - 1])
                break
            elif 49 == j:
                selected.append(animals[j])
    random.shuffle(selected)
    return selected


def crossover(selected):
    childs = []
    for i in range(0, 49, 2):
        split = random.randint(1, 6)
        genotype1 = []
        genotype2 = []
        for j in range(8):
            if j <= split:
                genotype1.append(selected[i].genotype[j])
                genotype2.append(selected[i + 1].genotype[j])
            else:
                genotype1.append(selected[i + 1].genotype[j])
                genotype2.append(selected[i].genotype[j])
        childs.append(Animal(genotype1))
        childs.append(Animal(genotype2))
    return childs


def Mutation(childs):
    for i in range(2):
        select = random.randint(0, len(childs) - 1)
        genotypeindex = random.randint(0, 7)
        randint = random.randint(0, 7)
        childs[select].genotype[genotypeindex] = randint


def generational_replacement(parents, children):
    maximum1 = 0
    maximum2 = 0
    for i in range(1, 49):
        if parents[maximum1].fit < parents[i].fit:
            if parents[maximum2].fit < parents[i].fit:
                maximum2 = i
            else:
                maximum1 = i
    children.append(parents[maximum1])
    children.append(parents[maximum2])
    return children


def steady_selection(animals):
    sum = 0
    chanses = []
    is_selected = [0] * 50
    selected = []
    for animal in animals:
        sum += animal.fit
    chanses.append(round(animals[0].fit / sum, 4))
    for i in range(1, 50):
        chanses.append(round(animal.fit / sum + chanses[i - 1], 4))
    counter = 0
    while counter != prep:
        randomnumber = round(random.uniform(0, 1), 5)
        for j in range(50):
            if chanses[j] >= randomnumber:
                if j == 0:
                    if is_selected[j == 0]:
                        selected.append(animals[j])
                        is_selected[j] = 1
                        counter += 1
                else:
                    if (j - 1) != 5:
                        selected.append(animals[j - 1])
                        is_selected[j - 1] = 1
                        counter += 1
                break
            elif 49 == j and is_selected[j] != 5:
                selected.append(animals[j])
                is_selected[j] = 1
                counter += 1
    return selected


def steady_replacement(parents, children):
    parents.sort(key=operator.attrgetter('fit'))
    del parents[:prep]
    selectedchilds = steady_selection(children)
    for select in selectedchilds:
        parents.append(select)
    return parents


def stop_condition(parents):
    for parent in parents:
        if 28 == parent.fit:
            print(parent.genotype)
            print(parent.fit)
            return False
    return True


def maingenetic():
    parents = initial()
    for i in parents:
        print(i.genotype)
    exit(0)
    for i in range(50):
        fitness(parents[i])
    counter = 0
    while stop_condition(parents):
        counter += 1
        selected = selection(list(parents))
        childs = crossover(list(selected))
        Mutation(childs)
        for i in childs:
            fitness(i)
        parents = steady_replacement(parents, childs)
    print("generation created")
    print(counter)


maingenetic()
