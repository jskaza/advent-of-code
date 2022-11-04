import numpy as np
import math

def func(x):
    return int(math.floor(x / 3 - 2 ))

vec_func = np.vectorize(func)

data = np.loadtxt("input.txt")

print(vec_func(data).sum())



