from shapely.geometry import Polygon
from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
def area(corner1, corner2, polygon):
    # Create rectangle from two opposite corners
    x1, y1 = corner1
    x2, y2 = corner2
    
    # Create rectangle corners in counter-clockwise order
    rect_corners = [
        (min(x1, x2), min(y1, y2)),  # bottom-left
        (max(x1, x2), min(y1, y2)),  # bottom-right
        (max(x1, x2), max(y1, y2)),  # top-right
        (min(x1, x2), max(y1, y2))   # top-left
    ]
    
    # Create rectangle polygon
    rect = Polygon(rect_corners)
    
    if polygon.covers(rect):
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        return width * height
    else:
        return 0

points = []
for line in lines:
    points.append(tuple(int(x) for x in line.split(",")))
polygon = Polygon(points)

print(max([area(c1, c2, polygon) for c1, c2 in combinations(points, 2)]))
