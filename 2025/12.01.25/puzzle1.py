with open("input.txt", "r") as f:
    lines = f.read().splitlines()

pos = 50
zeros = 0
for line in lines:
    direction, steps = line[0], int(line[1:])
    if direction == "R":
        pos = (pos + steps) % 100
    elif direction == "L":
        pos = (pos - steps) % 100
    if pos == 0:
        zeros += 1
print(zeros)
