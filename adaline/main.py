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

t = [1.0, -1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]

def maximum(a,b,c):
    max=-9999.0
    arr=[a,b,c]
    for i in arr:
        if(max< i):
            max=i
    return max



    return x

def posetive(num):
    if(num<0):
        return (-1*num)
    else:
        return num

w = [0.2, 0.2]
max = -9999.0
b = 0.0
alpha = 0.001
run = True

while (run):
    print("Ss")
    max=-9999
    for i in range(0, len(x) - 1):
        y_in = ((x[i][0] * w[0]) + (x[i][1] * w[1])+b)
        w0_temp=(alpha*(t[i]-y_in)*x[i][0])
        w1_temp=(alpha*(t[i]-y_in)*x[i][1])
        b_temp=(alpha * (t[i]-y_in))
        w[0]+=w0_temp
        w[1]+=w1_temp
        b+= b_temp
        max= maximum(max,posetive(w0_temp),posetive(w1_temp))
    print(max)

    if max < 0.007:
        run=False




print('w0 = {}'.format(w[0]))
print('w1 = {}'.format(w[1]))
print('b = {}'.format(b))

print("oh yessssssssssssss")

for i in range(0, len(x)):
    y = (x[i][0] * w[0]) + (x[i][1] * w[1]) + b
    if (y >= 0):
        print(' {} ,  {}'.format(t[i], "1"))
    else:
        print('{} , {}'.format(t[i], "-1"))

#for i in range(0,len(x)):
 #   plt.scatter(x[i][0],x[i][1], 10)

#x1= np.linspace(-1,1,100)
#x2=((-w[0]*x1)-b+teta)/w[1]

#x3=((-w[0]*x1)-b-teta)/w[1]

#plt.plot(x1, x2, '-r')
#plt.plot(x1, x3, '-r')
#plt.show()

