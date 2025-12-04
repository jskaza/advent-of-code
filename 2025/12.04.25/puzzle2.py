with open("input.txt", "r") as f:
    lines = f.read().splitlines()

rolls = 0
to_replace = []
while True:
    total_replacements = 0
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
                    to_replace.append((i, j))
                    total_replacements += 1
    for i,j in to_replace:
        lines[i] = list(lines[i])
        lines[i][j] = "x"
        lines[i] = "".join(list(lines[i]))
    if total_replacements == 0:
        x_count = 0
        for i in lines:
            x_count += i.count("x")
        print(x_count)
        break