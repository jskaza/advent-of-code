import math

with open("input.txt", "r") as f:
    lines = f.readlines()

def parser(line: str) -> int:
    sets = line.split(":")[1].split(";")
    sets = [x.strip().split(", ") for x in sets]
    cube_counts = {
    "red": 0,
    "green": 0,
    "blue": 0
    }
    for s in sets:
        for item in s:
            color = item.split(" ")[-1]
            ct = int(item.split(" ")[0])
            if  ct > cube_counts[color]:
                cube_counts[color] = ct
    return math.prod(list(cube_counts.values()))
    
sum_power = 0
for line in lines:
    sum_power += parser(line)
    
print(sum_power)