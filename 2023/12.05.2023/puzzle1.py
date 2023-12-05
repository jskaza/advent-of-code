import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

seeds = [int(x) for x in lines[0].split(": ")[1].split()]

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
        maps[current_map][range(source_start, source_start+range_len)] = dest_start - source_start
def get_location(seed: int) -> int:
    for _,v1 in maps.items():
        for k,v2 in v1.items():
            if seed in k:
                seed += v2
                break
    return seed

print(min([get_location(seed) for seed in seeds]))