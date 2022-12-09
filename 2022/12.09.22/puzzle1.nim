import strutils
import math
import sequtils

let input = splitLines(readFile("input.txt"))

var 
    head = (0,0)
    tail = (0,0)
    tails = @[(0,0)]

proc direction(x: string): char =
    return x[0]

proc magnitude(x: string): int =
    return parseInt(x[2..^1])

proc checkDistance(head, tail: tuple): bool =
    # don't feel like dealing with floating point issues
    return sqrt((float(head[0]) - float(tail[0]))^2 + (float(head[1]) - float(tail[1]))^2) > 1.5

proc updateTail(head: tuple, tail: var tuple): tuple =
    if head[0] > tail[0]:
        tail[0] += 1
    if head[0] < tail[0]:
        tail[0] -= 1
    if head[1] > tail[1]:
        tail[1] += 1
    if head[1] < tail[1]:
        tail[1] -= 1
    return tail

for line in input:
    let direction = direction(line)
    let magnitude = magnitude(line)
    case direction
    of 'U':
        head[1] += magnitude
    of 'D':
        head[1] -= magnitude
    of 'L':
        head[0] -= magnitude
    of 'R':
        head[0] += magnitude
    else:
        continue
    var update: bool = checkDistance(head, tail)
    while update:
        tail = updateTail(head, tail)
        tails.add(tail)
        update = checkDistance(head, tail)

echo len(deduplicate(tails))