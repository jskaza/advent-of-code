import std/strutils

let input = readFile("input.txt")

proc throwScore(line: string): int =
    result = case $line[^1]:
        of "X":
            1
        of "Y":
            2
        else:
            3
proc matchScore(line: string): int =
    if line == "A Y" or line == "B Z" or line == "C X":
        return 6
    elif line == "A Z" or line == "B X" or line == "C Y":
        return 0
    else:
        return 3

var total: int
for line in splitLines(input):
    total += throwScore(line) + matchScore(line)

echo(total)