with open("input.txt", "r") as f:
    lines = f.readlines()

cube_counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_set(s: list) -> bool:
    set_counts = dict(zip(cube_counts.keys(), [0]*3))
    for item in s:
        color = item.split(" ")[-1]
        set_counts[color] += int(item.split(" ")[0])
    for k,v in set_counts.items():
        if v > cube_counts[k]:
            return False
    return True

def parser(line: str) -> int:
    game_id = int(line.split(":")[0].split(" ")[1])
    sets = line.split(":")[1].split(";")
    sets = [x.strip().split(", ") for x in sets]
    for s in sets:
        if not check_set(s):
            return 0
    return game_id
    
sum_ids = 0
for line in lines:
    sum_ids += parser(line)
    
print(sum_ids)