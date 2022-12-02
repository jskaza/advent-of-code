import std/strutils

let input = readFile("input.txt")

proc throwScore(line: string): int =
   if line == "C Z" or line == "A Y" or line == "B X":
    return 1
   elif line == "A Z" or line == "B Y" or line == "C X":
    return 2
   else:
    return 3

proc matchScore(line: string): int =
    if $line[^1] == "X":
        return 0
    elif $line[^1] == "Y":
        return 3
    else:
        return 6

var total: int
for line in splitLines(input):
    total += throwScore(line) + matchScore(line)

echo(total)