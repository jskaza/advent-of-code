with open("input.txt", "r") as f:
    lines = f.read().splitlines()

ranges = []
for line in lines:
    if "-" in line:
        low, high = line.split("-")
        low = int(low)
        high = int(high)
        for i in ranges:
            if low >= i[0] and high <= i[1]:
                low = 1
                high = -1
            if low >= i[0] and low <= i[1]:
                low = i[1] + 1
            if high >= i[0] and high <= i[1]:
                high = i[0] - 1
            if low <= i[0] and high >= i[1]:
                ranges.remove(i)
        if low <= high:
            ranges.append((low, high))

print(sum([i[1] - i[0] + 1 for i in ranges]))