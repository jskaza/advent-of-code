with open("input.txt", "r") as f:
    strings = f.read().split(",")

def HASH(s):
    ct = 0
    for i in s:
        ct = (17*(ct + ord(i)))%256
    return ct

print(sum([HASH(s) for s in strings]))