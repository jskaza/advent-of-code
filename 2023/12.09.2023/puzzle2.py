import numpy as np

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [np.array([int(x) for x in line.split()]) for line in lines]

def extrapolate(line, vals=None):
    if vals == None:
        vals = [line[0]]
    else:
        vals.append(line[0])
    new_line = np.diff(line)
    if np.all(new_line == 0):
        val = vals[-1]
        for i in reversed(vals[:-1]):
            val = i - val
        return val
    else:
        return extrapolate(new_line, vals)

print(sum([extrapolate(line, []) for line in lines]))