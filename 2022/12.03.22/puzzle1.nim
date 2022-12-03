import std/strutils
import std/sequtils
import std/tables

let input = readFile("input.txt")

let
    lower =  {'a' .. 'z'}
    upper = {'A' .. 'Z'}
    nums = {1 .. 52}

var letters = newSeq[char]()
for l in lower.items:
    letters.add(l)
for u in upper.items:
    letters.add(u)

var priorities = newSeq[int]()
for n in nums.items:
    priorities.add(n)

var prioritiesTbl = initTable[char, int]()

for pairs in zip(letters, priorities):
  let (l, p) = pairs
  prioritiesTbl[l] = p

proc priority(line: string): int= 
    let splitPoint = int(len(line)/2)
    let comp1 = line[0 ..< splitPoint].toSeq()
    let comp2 = line[splitPoint .. ^1].toSeq()
    let overlap =  comp1.filterIt(it in comp2)[0]
    return prioritiesTbl[overlap]

var total: int
for line in splitLines(input):
    total += priority(line)

echo total
