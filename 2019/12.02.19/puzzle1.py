import pandas as pd

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

data = pd.read_csv("input.csv", sep=",", header=None).values.flatten()
data[1] = 12
data[2] = 2

i = 0
while i < len(data):
    if data[i] == 99:
        break
    else:
        data = opcode(data, i)
    i+=4

print(data[0])