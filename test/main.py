import numpy as np
import random

# learning_rate
learning_rate = 0.7

# import samples
data = np.genfromtxt('mlp.txt')
split = round(data.size * 0.7)
train, test = data[:split, :], data[split:, :]
prev_w = []
prev_v = []
prev_errors = []


# function for calc f
def f(x):
    return 1 / (1 + (1 / pow(2.71, x)))


# function for calc f prim
def fp(x):
    r = f(x)
    return r * (1 - r)


# function for checj stop condition
def check_stop_condition(currentW, currentV, tests):
    current_errors_count = use(currentV, currentW, tests)
    prev_v.append(currentV)
    prev_w.append(currentW)
    prev_errors.append(current_errors_count)
    prev_errors_count = len(prev_errors)
    if prev_errors_count > 5:
        prev_errors.pop(0)
        prev_v.pop(0)
        prev_w.pop(0)
    for i in range(prev_errors_count - 1):
        if prev_errors[i] < prev_errors[i + 1]:
            return True
        return False


# main section of the program
v = []
w = []
# step 0 init weights
for i in range(12):
    v.append(round(random.uniform(-0.5, 0.5), 3))
for i in range(5):
    w.append(round(random.uniform(-0.5, 0.5), 3))
# step 1
stop_condition = False

while not stop_condition:
    # step 2
    for x in train:
        # step 3
        z = []
        for j in range(4):
            # step 4
            sigma = 0
            for i in range(2):
                index = (i + 1) * 4 + j
                sigma += x[i] * v[index]
            zin = sigma + v[j]
            z.append(f(zin))
        ###############  step 5  ##############
        sigma = 0
        for i in range(4):
            index = i + 1
            sigma += x[i] * w[index]
        yin = sigma + w[j]
        y = f(yin)
        ############### step 6  ##############
        delta_k = (x[2] - y) * fp(yin)
        deltaW = []
        deltaW.append(learning_rate * delta_k)
        for i in range(4):
            deltaW.append(z[i] * learning_rate * delta_k)
        ###############  step 7  ###############
        delta_in_j = []
        for i in range(4):
            delta_in_j[i] = delta_k * w[i + 1]
        delta_j = []
        for i in range(4):
            delta_j[i] = delta_in_j[i] * fp(zin[j])

        delta_v = []
        for i in range(4):
            delta_v[i] = learning_rate * delta_j[i]
            delta_v[i + 4] = learning_rate * delta_j[i] * x[0]
            delta_v[i + 8] = learning_rate * delta_j[i] * x[1]
        # step 8
        for i in range(5):
            w[i] += deltaW
        for i in range(12):
            v[i] += delta_v[i]
    stop_condition = check_stop_condition(w[:], v[:], test)


def use(w, v, samples):
    count_errors = 0
    # step 0 , 1 ,2
    for x in samples:
        # step 3
        z = []
        for i in range(4):
            sigma = 0
            for j in range(2):
                index = (j + 1) * 4 + i
                sigma += x[j] * v[index]
            z_in_j = v[i] + sigma
            z.append(f(z_in_j))
        sigma = 0
        for i in range(4):
            index = i + 1
            sigma += z[i] * w[index]
        y = f(w[0] + sigma)
        if y != x[2]:
            count_errors += 1
    return count_errors
