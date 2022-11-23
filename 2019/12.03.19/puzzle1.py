import pandas as pd
import numpy as np

data = pd.read_csv("input.csv", sep=",", header=None).values


def path(instructions: np.array) -> list:
    current = [0, 0]
    res = []
    for i in range(len(instructions)):
        direction = instructions[i][0]
        magnitude = int(instructions[i][1:])
        if direction == "L":
            to_add = list(
                zip(range(current[0] - magnitude, current[0]), [current[1]] * magnitude))
            current[0] = current[0] - magnitude
        elif direction == "R":
            to_add = list(zip(range(current[0] + 1, current[0] +
                                    magnitude + 1), [current[1]] * magnitude))
            current[0] = current[0] + magnitude
        elif direction == "U":
            to_add = list(zip([current[0]] * magnitude, range(current[1] + 1, current[1] +
                                                              magnitude + 1)))
            current[1] = current[1] + magnitude
        elif direction == "D":
            to_add = list(zip([current[0]] * magnitude, range(current[1] -
                                                              magnitude, current[1])))
            current[1] = current[1] - magnitude
        res = res + to_add
    return res


wire1 = path(data[0])
wire2 = path(data[1])

intersections = list(set(wire1) & set(wire2))

print(min(map(lambda x: np.abs(x[0]) + np.abs(x[1]), intersections)))
