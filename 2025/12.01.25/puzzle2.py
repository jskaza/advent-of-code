with open("input.txt", "r") as f:
    lines = f.read().splitlines()

pos = 50
hit_zero = 0
for line in lines:
    prev_pos = pos
    direction, steps = line[0], int(line[1:])
    if direction == "R":
        pos += steps
    elif direction == "L":
        pos -= steps
    if direction == "R":
        for i in range(prev_pos+1, pos+1):
            if i%100 == 0:
                hit_zero += 1
    elif direction == "L":
        for i in range(prev_pos-1, pos-1, -1):
            if i%100 == 0:
                hit_zero += 1
print(hit_zero)