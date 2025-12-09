from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
def area(corner1, corner2):
    return abs(corner1[0] - corner2[0] + 1) * abs(corner1[1] - corner2[1] + 1)
corners = []
for line in lines:
    corners.append(tuple(int(x) for x in line.split(",")))

print(max([area(c1, c2) for c1, c2 in combinations(corners, 2)]))
