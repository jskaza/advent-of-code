import numpy as np

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [np.array([int(x) for x in line.split()]) for line in lines]

def extrapolate(line, init=0):
    init += line[-1]
    new_line = np.diff(line)
    if np.all(new_line == 0):
        return init
    else:
        return extrapolate(new_line, init)

print(sum([extrapolate(line) for line in lines]))