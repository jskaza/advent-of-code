
import numpy as np

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
def calc_copies(line):
    line = line.split(": ")[1]
    nums = line.split(" | ")
    winning_nums = [int(num) for num in nums[0].split()]
    my_nums = [int(num) for num in nums[1].split()]
    ct = 0
    for num in winning_nums:
        if num in my_nums:
            ct+=1
    return ct

cards = np.ones(len(lines), int)

for idx, line in enumerate(lines):
    copies = calc_copies(line)
    cards[idx+1:idx+copies+1] += cards[idx]

print(cards.sum())