import std/strutils
import std/algorithm
import std/math

let input = readFile("input.txt")

var
  cals = @[0]

for line in splitLines(input):
    if line == "":
        cals.add(0)
    else:
        cals[^1] += parseInt(line)

cals.sort()

echo(sum(cals[^3 .. ^1]))