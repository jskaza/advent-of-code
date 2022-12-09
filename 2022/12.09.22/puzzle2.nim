import strutils
import math
import tables
import sequtils

let input = splitLines(readFile("input.txt"))

var 
    ropes =  {0: (0,0), 1: (0,0), 2: (0,0), 3: (0,0), 4: (0,0), 5: (0,0), 6: (0,0), 7: (0,0), 8: (0,0), 9: (0,0)}.toTable
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
        ropes[0][1] += magnitude
    of 'D':
        ropes[0][1] -= magnitude
    of 'L':
        ropes[0][0] -= magnitude
    of 'R':
        ropes[0][0] += magnitude
    else:
        continue
    var updateRope: bool = checkDistance(ropes[0], ropes[1])
    while updateRope:
        var updates = 0
        for r in 1..9:
            if checkDistance(ropes[r-1], ropes[r]):
                ropes[r] = updateTail(ropes[r-1], ropes[r])
                updates += 1
            if r == 9:
                tails.add(ropes[9])
        if updates == 0:
            updateRope = false

echo len(deduplicate(tails))