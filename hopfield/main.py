import numpy as np
import random

arr = np.genfromtxt('plus.txt')
# step0 initialize weight using heb rules
x = np.array([1, -1, -1, -1, 1,
              -1, 1, -1, 1, -1,
              -1, -1, 1, -1, 1,
              -1, 1, -1, 1, -1,
              1, -1, -1, -1, 1])[np.newaxis]
o = np.array([-1, 1, 1, 1, -1,
              1, -1, -1, -1, 1,
              1, -1, -1, -1, 1,
              1, -1, -1, -1, 1,
              -1, 1, 1, 1, -1])[np.newaxis]
plus = np.array([-1, -1, 1, -1, -1,
                 -1, -1, 1, -1, -1,
                 1, 1, 1, 1, 1,
                 -1, -1, 1, -1, -1,
                 -1, -1, 1, -1, -1])[np.newaxis]
deltaW = np.matmul(x.T, x)
deltaW = np.add(deltaW, np.matmul(o.T, o))
deltaW = np.add(deltaW, np.matmul(plus.T, plus))
for i in range(25):
    deltaW[i, i] = 0
    arr[i, i] = 0
if (deltaW==arr).all():
    print("ok")
else:
    print("NOK")
# step 1 to 6 using of hopfield
def hopfielduse(inputkar):
    # step1 and step2
    y = list(inputkar)
    # step3
    # randomize the unit orders
    r = list(range(25))
    random.shuffle(r)
    # step 4-6
    for i in r:
        # step4
        sigma = 0
        for j in range(25):
            sigma += y[j] * deltaW[j][i]
        yin = inputkar[i] + sigma
        # step5
        if yin > 0:
            y[i] = 1
        elif yin < 0:
            y[i] = 0
    return y


# step 7 and loop back
flag = True
epoch = 0
inputuser = [0, 0, 1, 0, 0,
             1, 0, 0, 0, 0,
             1, 0, 0, 0, 1,
             1, 0, 0, 0, 0,
             0, 0, 0, 0, 0]
inputtemp = list(inputuser)
inputView = np.reshape(np.asarray(inputuser), (-1, 5))
res = []
while flag:
    epoch = 1 + epoch
    res = hopfielduse(inputuser)
    if res == inputtemp:
        flag = False
    else:
        inputtemp = list(res)

resView = np.reshape(res, (-1, 5))
