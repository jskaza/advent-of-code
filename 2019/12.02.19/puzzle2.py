import pandas as pd

data = pd.read_csv("input.csv", sep=",", header=None).values.flatten()


def opcode(data, idx):
    op = data[idx]
    pos1 = data[data[idx+1]]
    pos2 = data[data[idx+2]]
    output = data[idx+3]
    if op == 1:
        data[output] = pos1+pos2
    elif op == 2:
        data[output] = pos1*pos2
    return data


for i in range(100):
    for j in range(100):
        temp = data.copy()
        temp[1] = i
        temp[2] = j
        k = 0
        while k < len(temp):
            if temp[k] == 99:
                break
            else:
                temp = opcode(temp, k)
                k += 4
        if temp[0] == 19690720:
            print(100*i+j)
            break
    else:
        continue
    break
