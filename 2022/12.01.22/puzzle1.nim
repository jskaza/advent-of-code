import std/strutils

let input = readFile("input.txt")

var
  cals = @[0]

for line in splitLines(input):
    if line == "":
        cals.add(0)
    else:
        cals[^1] += parseInt(line)

echo(max(cals))