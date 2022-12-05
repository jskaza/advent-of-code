import std/strutils
import std/tables
import std/sequtils
import std/algorithm

let input = readFile("input.txt")

var
    stackRows: seq[string]
    stacks = initTable[int, seq[char]]()
    instructions: seq[string]
    sep: bool = false


# get data in correct format
for line in splitLines(input):
    if startswith(line, " 1") or line == "":
        sep = true
        continue
    if sep:
        instructions.add(line)
    else:   
        stackRows.add(line & " ")

for row in stackRows:
    var stack: int
    # 4 chars per stack `[A] `
    for i in countup(0, len(row) - 1, 4):
        stack += 1
        let text = row[i .. i+3]
        if strip(text) == "":
            continue
        else:
            if not stacks.hasKey(stack):
                stacks[stack] = @[]
            stacks[stack].insert(text[1], 0)

for i in instructions:
    let parsed = split(i, " ")
    let numToMove = parseInt(parsed[1])
    let binFrom = parseInt(parsed[3])
    let binTo = parseInt(parsed[5])
    stacks[binTo].add((stacks[binFrom][^numToMove .. ^1]).reversed())
    stacks[binFrom].delete((len(stacks[binFrom]) - numToMove)..<len(stacks[binFrom]))
    
var index: seq[int]
for i in stacks.keys:
    index.add(i)
index.sort()

var res: string
for i in index:
    res.add($stacks[i][^1])

echo res