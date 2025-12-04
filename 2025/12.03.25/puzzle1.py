with open("input.txt", "r") as f:
    lines = f.read().splitlines()

score = 0
for line in lines:
    candidates = []
    for i in range(len(line)-1):
        candidates += [int(line[i]+line[j]) for j in range(i+1, len(line))]
    score+= max(candidates)

print(score)






