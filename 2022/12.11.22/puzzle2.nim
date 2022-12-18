import strutils
# neat little mathematical expression evaluator library 
# https://yardanico.github.io/nim-mathexpr/mathexpr.html
import mathexpr
import math
import algorithm

let input = readFile("input.txt")

type
  Monkey = object
    items: seq[string]
    operation: string
    test: float
    ifTrue: int
    ifFalse: int

var 
    monkeys: seq[Monkey]

const rounds = 10000

proc parseItems(s: string): seq[string] =
    let itemsStr = s.split(": ")[1]
    return itemsStr.split(", ")

proc parseOp(s: string): string =
    return s.split("= ")[1]

proc parseTest(s: string): float =
    return parseFloat(s.split("by ")[1])

proc parseThrow(s: string): int =
    return parseInt($s[^1])

proc performOp(op, old: string, modulo: float): float =
    let ev = newEvaluator()
    return ev.eval(op.replace("old", old)) mod modulo

for line in splitLines(input):
    if line.startsWith("M"):
        monkeys.add(Monkey())
    elif line.contains("Starting"):
        monkeys[^1].items = parseItems(line)
    elif line.contains("Operation"):
        monkeys[^1].operation = parseOp(line)
    elif line.contains("Test"):
        monkeys[^1].test = parseTest(line)
    elif line.contains("true"):
        monkeys[^1].ifTrue = parseThrow(line)
    elif line.contains("false"):
         monkeys[^1].ifFalse = parseThrow(line)
    else:
        continue

var inspections = newSeq[int](len(monkeys))
var modulo:float = 1
for monkey in monkeys: 
    modulo = modulo * monkey.test

for i in 1..rounds:
    for idx, monkey in monkeys:
        for item in monkey.items:
            inspections[idx] += 1
            let worryLevel = performOp(monkey.operation, item, modulo)
            if (worryLevel mod monkey.test) == 0:
                monkeys[monkey.ifTrue].items.add($worryLevel)
            else:
                monkeys[monkey.ifFalse].items.add($worryLevel)
        
        monkeys[idx].items = @[] # important to reset after each round

inspections.sort()

echo inspections[^1] * inspections[^2]