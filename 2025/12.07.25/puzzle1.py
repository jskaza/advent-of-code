with open("input.txt", "r") as f:
    lines = f.read().splitlines()

active_positions = [lines[0].index("S")]
splits = 0
for line in lines[1:]:
    splitters = [i for i, letter in enumerate(line) if letter == "^"]
    for i in splitters:
        if i in active_positions:
            splits += 1
            active_positions.remove(i)
            if i-1 not in active_positions:
                active_positions.append(i-1) 
            if i+1 not in active_positions:
                active_positions.append(i+1)
print(splits)