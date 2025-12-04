with open("input.txt", "r") as f:
    lines = f.read().replace("\n", "").split(",")


invalid = 0
for line in lines:
    low, high = line.split("-")
    for i in range(int(low), int(high)+1):
        if (str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]):
            invalid += int(i)
    
print(invalid)