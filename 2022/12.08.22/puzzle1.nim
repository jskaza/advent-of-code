import strutils
import sequtils

let input = splitLines(readFile("input.txt"))
var nVisible: int

for idx,line in input[1..^2]:
    let heightsChar = line.toSeq()
    var heights: seq[int]
    for h in heightsChar:
        heights.add(parseInt($h))
    for i in countup(1,len(line)-2):
        let treeHeight = heights[i]
        if treeHeight > max(heights[0..<i]):
            nVisible += 1
        elif treeHeight > max(heights[i+1..^1]):
            nVisible += 1
        else:
            var heightsAbove: seq[int]
            var heightsBelow: seq[int]
            for l in input[0..<idx+1]:
                heightsAbove.add(parseInt($l[i]))
            for l in input[idx+2..^1]:
                heightsBelow.add(parseInt($l[i]))
            if treeHeight > max(heightsAbove):
                nVisible += 1
            elif treeHeight > max(heightsBelow):
                nVisible += 1

# - 4 to avoid double counting corner trees
echo 2*len(input) + 2*len(input[0]) - 4 + nVisible


