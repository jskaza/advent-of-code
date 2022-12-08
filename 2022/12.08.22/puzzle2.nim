import strutils
import sequtils
import algorithm

let input = splitLines(readFile("input.txt"))

var maxScore: int

proc treesSeen(x: int, view: seq[int]): int = 
    var n: int
    for i in view:
        n += 1
        if i >= x:
            break
    return n

proc scenicScore(x: int, l, r, a, b: seq[int]): int =
    let leftSeen = treesSeen(x, l.reversed())
    let rightSeen = treesSeen(x, r)
    let aboveSeen = treesSeen(x, a.reversed())
    let belowSeen = treesSeen(x, b)
    return leftSeen * rightSeen * aboveSeen * belowSeen

# edge trees will have scenic score = 0
for idx,line in input[1..^2]:
    let heightsChar = line.toSeq()
    var heights: seq[int]
    for h in heightsChar:
        heights.add(parseInt($h))
    for i in countup(1,len(line)-2):
        let treeHeight = heights[i]
        let heightsLeft = heights[0..<i]
        let heightsRight= heights[i+1..^1]
        var heightsAbove: seq[int]
        var heightsBelow: seq[int]
        for l in input[0..<idx+1]:
            heightsAbove.add(parseInt($l[i]))
        for l in input[idx+2..^1]:
            heightsBelow.add(parseInt($l[i]))
        let score = scenicScore(treeHeight, heightsLeft, heightsRight, heightsAbove, heightsBelow)
        if score > maxScore:
            maxScore = score

echo maxScore

