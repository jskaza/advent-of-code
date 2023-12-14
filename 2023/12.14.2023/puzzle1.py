with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
grid = [""]*len(lines[0])

for i in range(len(lines[0])):
    for j in lines:
        grid[i] += j[i]
    grid[i] = grid[i].replace(".", "Z")
    grid[i] = [sorted(x) for x in grid[i].split("#")]
    if len(grid[i]) > 0:
        for k in range(1, len(grid[i])):
            grid[i][k] = ["Z"] + grid[i][k]
    grid[i] = list(reversed([x for items in grid[i] for x in items]))
    grid[i] = sum([x+1 if grid[i][x] == "O" else 0 for x in range(len(grid[i]))])

print(sum(grid))
        