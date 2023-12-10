import networkx as nx
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]

def pass_through(row, col, coming_from=None):
    tile = lines[row][col]
    if tile == "S":
        lines[row][col] = "T"
        if lines[row+1][col] == "|":
            row += 1
            coming_from = "N"
        elif lines[row+1][col] == "L":
            row += 1
            coming_from = "W"
        elif lines[row+1][col] == "J":
            row += 1
            coming_from = "E"
        elif lines[row][col+1] == "-":
            col += 1
            coming_from = "W"
        elif lines[row][col+1] == "7":
            col += 1
            coming_from = "N"
        elif lines[row][col+1] == "J":
            col += 1
            coming_from = "S"
        elif lines[row][col-1] == "-":
            col -= 1
            coming_from = "E"
        elif lines[row][col-1] == "L":
            col -= 1
            coming_from = "S"
        elif lines[row][col-1] == "F":
            col -= 1
            coming_from = "N"
    elif tile == "|":
        if coming_from == "N":
            row += 1
        else:
            row -= 1
    elif tile == "-":
        if coming_from == "E":
            col -= 1
        else: 
            col += 1
    elif tile == "L":
        if coming_from == "N":
            col += 1
            coming_from = "W"
        else:
            row -= 1
            coming_from = "S"
    elif tile == "J":
        if coming_from == "N":
            col -= 1
            coming_from = "E"
        else:
            row -= 1
            coming_from = "S"
    elif tile == "7":
        if coming_from == "S":
            col -= 1
            coming_from = "E"
        else:
            row += 1
            coming_from = "N"
    elif tile == "F":
        if coming_from == "S":
            col += 1
            coming_from = "W"
        else:
            row += 1
            coming_from = "N"
    return tile, row, col, coming_from

for row, line in enumerate(lines):
    for col, tile in enumerate(line):
        if tile == "S":
            coming_from = None
            ct = 0
            while  tile != "T":
                tile, row, col, coming_from = pass_through(row, col, coming_from)
                ct += 1
            break
print(int((ct-1)/2))
