with open("input.txt", "r") as f:
    lines = f.read().replace("\n", "").split(",")


invalid = 0
for line in lines:
    low, high = line.split("-")
    for i in range(int(low), int(high)+1):
        s = str(i)
        l = len(s)
        if l > 1:
            half = l//2
            for j in range(1, half+1):
                if l % j == 0:
                    chunks = [s[k:k+j] for k in range(0, l, j)]
                    if all(chunk == chunks[0] for chunk in chunks):
                        invalid += i
                        break

print(invalid)