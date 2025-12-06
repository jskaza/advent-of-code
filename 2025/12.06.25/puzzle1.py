import numpy as np
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
ops = lines[-1].split()
total = 0
for pos, op in enumerate(ops):
    nums = np.array([int(line.split()[pos]) for line in lines[:-1]])
    if op == "+":
        total += np.sum(nums)
    elif op == "*":
        total += np.prod(nums)
        
print(total)
        