import strutils

let input = splitLines(readFile("input.txt"))

var 
    X = @[1]
    idx = 0
    addx: bool
    pixels = newSeq[string](240)


proc parseInstruction(s: string): int =
    return parseInt(s.split(" ")[1])

var pixel: int
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
    if abs((pixel mod 40) - X[pixel]) <= 1:
        pixels[pixel] = "#"
    else:
        pixels[pixel] = "."
    pixel += 1

for i in countup(0, 200, 40):
    echo pixels[i..i+39].join("")