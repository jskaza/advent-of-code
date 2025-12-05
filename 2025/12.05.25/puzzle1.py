with open("input.txt", "r") as f:
    lines = f.read().splitlines()

ranges = []
ingredients = []
for line in lines:
    if "-" in line:
        low, high = line.split("-")
        ranges.append((int(low), int(high)))
    elif line.isdigit():
        ingredients.append(int(line))

def check_ingredient(ingredient: int, ranges: list) -> bool:
    for range in ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True
    return False

fresh = 0
for ingredient in ingredients:
    fresh += check_ingredient(ingredient, ranges)

print(fresh)