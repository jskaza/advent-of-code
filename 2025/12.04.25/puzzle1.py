with open("input.txt", "r") as f:
    lines = f.read().splitlines()

rolls = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "@":
            adjacents = 0
            try:
                adjacents += lines[i-1][j-1] == "@"and i-1 >= 0 and j-1 >= 0
            except:
                adjacents += 0
            try:
                adjacents += lines[i-1][j] == "@"and i-1 >= 0
            except:
                adjacents += 0
            try:
                adjacents += lines[i-1][j+1] == "@" and i-1 >= 0
            except:
                adjacents += 0
            try:
                adjacents += lines[i][j-1] == "@" and j-1 >= 0
            except:
                adjacents += 0
            try:
                adjacents += lines[i][j+1] == "@"
            except:
                adjacents += 0
            try:
                adjacents += lines[i+1][j-1] == "@" and j-1 >= 0
            except:
                adjacents += 0
            try:
                adjacents += lines[i+1][j] == "@"
            except:
                adjacents += 0
            try:
                adjacents += lines[i+1][j+1] == "@"
            except:
                adjacents += 0
            if adjacents < 4:
                rolls += 1
print(rolls)
