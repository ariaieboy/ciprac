import matplotlib.pyplot as plt
import numpy as np

x = [
    [0.67044, -0.437],
    [-0.35508, -0.53923],
    [0.10452, 0.42226],
    [0.95826, 0.24915],
    [0.098617, 0.18122],
    [-0.33915, 0.32088],
    [0.23894, -0.90489],
    [-0.27873, -0.30243],
    [0.51302, -0.097319],
    [-0.1722, -0.51819],
    [-0.01531, 0.43009],
    [0.38949, 0.71236],
    [0.94547, -0.43698],
    [-0.34449, 0.4621],
    [0.67561, -0.72447],
    [0.47814, 0.67345],
    [0.90835, -0.7228],
    [-0.93615, 0.17642],
    [-0.28626, -0.26769],
    [0.32531, 0.61352]]

t = [1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1]

# x1    x2    x3      y
# 0.2  0.5   0.1     -1
# 0.1  0.7   0.8      1
# -0.1  0.6   0.9      1
# -0.8  0.5   0.1     -1
# -0.7  0.9  -0.1     -1
# 0.3  0.1   0.6      1

w = [0, 0]

b = 0
teta = 0.1
alpha = 2
run = True

while (run):
    y_in = 0
    run = False
    for i in range(0, len(x) - 1):
        y_in = (x[i][0] * w[0]) + (x[i][1] * w[1]) + b
        y = 0
        if (y_in < -teta):
            y = -1
        elif (y_in > teta):
            y = 1
        if (t[i] != y):
            w[0] += (alpha * t[i] * x[i][0])
            w[1] += (alpha * t[i] * x[i][1])
            b += (alpha * t[i])
            run = True

print('w0 = {}'.format(w[0]))
print('w1 = {}'.format(w[1]))
print('b = {}'.format(b))

for i in range(0, len(x)):
    y = (x[i][0] * w[0]) + (x[i][1] * w[1]) + b
    if (y >= 0):
        print(' {} ,  {}'.format(t[i], "1"))
    else:
        print('{} , {}'.format(t[i], "-1"))

for i in range(0,len(x)):
    plt.scatter(x[i][0],x[i][1], 10)

x1= np.linspace(-1,1,100)
x2=((-w[0]*x1)-b+teta)/w[1]

x3=((-w[0]*x1)-b-teta)/w[1]

plt.plot(x1, x2, '-r')
plt.plot(x1, x3, '-r')
plt.show()

