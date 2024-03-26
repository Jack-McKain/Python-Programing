import numpy as np
import matplotlib.pyplot as plt
from random import random, randint

'''x = np.arange(0,10,.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()'''


# Three corners of an random triangle
corner = [(random(), random()),
(random(),random()), (random(),random())]
def midpoint(p, q):
 return (0.5*(p[0] + q[0]),
 0.5*(p[1] + q[1]))
N = 10000
x = np.zeros(N)
y = np.zeros(N)
x[0] = random()
y[0] = random()
for i in range(1, N):
 k = randint(0, 2)
 x[i], y[i] = midpoint( corner[k],
(x[i-1], y[i-1]) )
plt.scatter(x, y, s=0.01, c="red")
plt.show()