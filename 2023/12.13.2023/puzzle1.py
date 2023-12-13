import numpy as np

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

patterns = [[]]
for line in lines:
    if line == "":
        patterns.append([])
        continue
    patterns[-1].append(list(line))

patterns = [np.array(pattern) for pattern in patterns]

def find_reflection(pattern):
    for row in range(pattern.shape[0]-1):
        reflection = min(row+1, pattern.shape[0] - row - 1)
        if np.all(pattern[row+1-reflection:row+1,] == np.flip(pattern[row+1:row+1+reflection,:], axis=0)):
            return 100*(row+1)
    for col in range(pattern.shape[1]-1):
        reflection = min(col+1, pattern.shape[1] - col - 1)
        if np.all(pattern[:,col+1-reflection:col+1] == np.flip(pattern[:,col+1:col+1+reflection],axis=1)):
            return col+1

print(sum([find_reflection(pattern) for pattern in patterns]))
        