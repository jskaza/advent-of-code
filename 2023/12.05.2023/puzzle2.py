import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

ranges = [int(x) for x in lines[0].split(": ")[1].split()]
seed_ranges = []
for r in range(0,len(ranges),2):
    seed_ranges.append((ranges[r], ranges[r]+ranges[r+1]-1))

maps = {}
for line in lines[2:]:
    line_start = re.match("[a-z]*-[a-z]*-[a-z]*", line)
    if line_start is not None:
        current_map = line_start[0]
        maps[current_map] = {}
    elif line == "":
        continue
    else:
        dest_start, source_start, range_len = [int(x) for x in line.split()]
        maps[current_map][(source_start, source_start+range_len-1)] = dest_start - source_start

def range_intersect(r1: tuple, m: dict) -> list:
    new = []
    intersections = []
    for r2, v in m.items():
        start = max(r1[0],r2[0])
        end = min(r1[1],r2[1])
        if start <= end:
            new.append((start+v, end+v))
            intersections.append((start, end))
        else:
            continue
    if len(intersections) == 0:
        return [r1]
    else:
        intersections = sorted(intersections, key = lambda x: x[0])
        if intersections[0][0] > r1[0]:
            new.append((r1[0],intersections[0][0]-1))
            intersections = [(r1[0],intersections[0][0]-1)] + intersections
        if intersections[-1][1] < r1[1]:
            new.append((intersections[-1][1]+1, r1[1]))
            intersections.append((intersections[-1][1]+1, r1[1]))
        for idx in range(len(intersections)-1):
            if intersections[idx][1] + 1 != intersections[idx+1][0]:
                new.append((intersections[idx][1] + 1, intersections[idx+1][0] - 1))

    return new

def get_location(r: tuple) -> int:
    ranges = [r]
    for temp,v1 in maps.items():
        # print(v1)
        new_ranges = []
        for s in ranges:
            # print(s)
            new_ranges += range_intersect(s, v1)
        ranges = new_ranges
    return min(ranges, key=lambda x: x[0])[0]

print(min([get_location(x) for x in  seed_ranges]))