import strutils
import json
import re

let input = readFile("input.txt")

type
    listPair = object
      list1: JsonNode
      list2: JsonNode
var 
    tracker: bool
    newPair: listPair
    sumIdx: int
    idx: int

let regex = re("(\\d+|\\[\\])")

proc compare(p: listPair): int = 
    echo p
    if p.list1.kind == JArray and p.list2.kind == JInt:
        if len(p.list1) == 0:
            return 1
        # flatten potentially nested array and perform some logic to determine result
        let list1Parsed = findAll($p.list1, regex)[0]
        if list1Parsed == "[]":
            return 1
        let list1Int = parseInt(list1Parsed)
        if p.list2.getInt() > list1Int:
            return 1
        elif p.list2.getInt() < list1Int:
            return -1
        elif list1Int == p.list2.getInt() and len(p.list1) > 1:
            return -1
        else:
            return 0
    if p.list1.kind == JInt and p.list2.kind == JArray:
        if  len(p.list2) == 0:
            return -1
        let list2Parsed = findAll($p.list2, regex)[0]
        if list2Parsed == "[]":
            return -1
        let list2Int = parseInt(list2Parsed)
        if  list2Int < p.list1.getInt():
            return -1
        elif list2Int > p.list1.getInt():
            return 1
        elif list2Int == p.list1.getInt() and len(p.list2) > 1:
            return 1
        else:
            return 0
    else:
        if len(p.list1) == 0 and len(p.list2) > 0:
            return 1
        for i in 0..<len(p.list1):
            if i >= len(p.list2):
                return -1
            elif p.list1[i].kind == JArray or p.list2[i].kind == JArray:
                let n = listPair(list1: p.list1[i], list2: p.list2[i])
                let r = compare(n) 
                if r != 0:
                    return r
                else:
                    continue
            elif p.list2[i].getInt() > p.list1[i].getInt():
                return 1
            elif p.list2[i].getInt() < p.list1[i].getInt():
                return -1
            if (i == len(p.list1) - 1 and len(p.list2) > len(p.list1)):
                return 1
            else:
                continue
for line in splitLines(input):
    if line == "":
        continue
    elif tracker:
        newPair.list2 = parseJson(line)
        if compare(newPair) >= 0:
            sumIdx += idx
    else:
       idx += 1
       newPair = listPair(list1: parseJson(line))
    tracker = not tracker

echo sumIdx