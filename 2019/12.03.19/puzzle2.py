import pandas as pd
import numpy as np

data = pd.read_csv("input.csv", sep=",", header=None).values


def path(instructions: np.array) -> dict:
    current = [0, 0]
    res = {}
    step = int(1)
    for i in range(len(instructions)):
        direction = instructions[i][0]
        magnitude = int(instructions[i][1:])
        if direction == "L":
            to_add = list(
                zip(range(current[0] - magnitude, current[0]),
                    [current[1]] * magnitude))
            current[0] = current[0] - magnitude
        elif direction == "R":
            to_add = list(zip(range(current[0]+1, current[0] +
                                    magnitude+1), [current[1]] * magnitude))
            current[0] = current[0] + magnitude
        elif direction == "U":
            to_add = list(zip([current[0]] * magnitude, range(current[1]+1, current[1] +
                                                              magnitude + 1)))
            current[1] = current[1] + magnitude
        elif direction == "D":
            to_add = list(zip([current[0]] * magnitude, range(current[1] -
                                                              magnitude, current[1])))
            current[1] = current[1] - magnitude
        for j, k in zip(to_add, range(step, step+magnitude)):
            if j not in res:
                res[j] = k
        step += magnitude
    return res


wire1 = path(data[0])
wire2 = path(data[1])

intersections = list(set(wire1.keys()) & set(wire2.keys()))

current_min = wire1[intersections[0]] + wire2[intersections[0]]
for i in intersections[1:]:
    steps = wire1[i] + wire2[i]
    if steps < current_min:
        current_min = steps

print(current_min)
