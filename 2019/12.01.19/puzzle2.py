import numpy as np
import math

def func(x):
    val = int(math.floor(x / 3 - 2 ))
    if val <= 0:
        return 0
    else:
        return val

vec_func = np.vectorize(func)

data = np.loadtxt("input.txt")

total = 0
while data.sum() > 0:
    data = vec_func(data)
    total += data.sum()


print(total)



