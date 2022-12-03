import std/strutils
import std/sequtils
import std/tables
import std/sets

let input = splitLines(readFile("input.txt"))

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

var total: int
for n in countup(0, len(input)-1, 3):
    let letter = input[n].toHashSet() * input[n+1].toHashSet() * input[n+2].toHashSet()
    total += prioritiesTbl[toSeq(letter)[0]]

echo total
