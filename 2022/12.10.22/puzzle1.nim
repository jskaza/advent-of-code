import strutils

let input = splitLines(readFile("input.txt"))

var 
    X = @[1]
    idx = 0
    addx: bool


proc parseInstruction(s: string): int =
    return parseInt(s.split(" ")[1])


while idx < len(input):
    if input[idx] == "noop":
        X.add(X[^1])
        idx += 1
    elif addx:
        X.add(X[^1] + parseInstruction(input[idx]))
        addx = false
        idx += 1
    else:
        X.add(X[^1])
        addx = true

var ss: int
for i in countup(20,220,40):
    ss += i*X[i-1] # i-1 represents during cycle

echo ss