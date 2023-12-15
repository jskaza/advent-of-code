with open("input.txt", "r") as f:
    strings = f.read().split(",")

def HASH(s):
    ct = 0
    for i in s:
        ct = (17*(ct + ord(i)))%256
    return ct

boxes = [None]*256

for s in strings:
    if s[-1] == "-":
        box = HASH(s[:-1])
        if boxes[box] is None:
            continue
        else:
            for b in boxes[box]:
                if b[0] == s[:-1]:
                    boxes[box].remove(b)
                    break
    else:
        label = s.split("=")[0]
        box = HASH(label)
        focal = int(s.split("=")[1])
        if boxes[box] is None:
            boxes[box] = [(label, focal)]
        elif sum([x[0] == label for x in boxes[box]]) == 0:
            boxes[box].append(tuple([label, focal]))
        else:
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i] = tuple([label, focal])
                    break
                
total = 0
for i,j in enumerate(boxes):
    if j is not None:
        for k,l in enumerate(j):
            total+=(i+1)*(k+1)*l[1]       
print(total)