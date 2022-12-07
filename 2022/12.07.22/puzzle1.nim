import std/strutils
import std/tables
import std/re

let input = readFile("input.txt")

var currentDirs: seq[string] 
var dirs = initTable[string, int]()
var ls: bool
let regex = re("\\d")
var dir: string

for line in splitLines(input):
    if line == "$ cd ..":
        ls = false
        currentDirs.delete(len(currentDirs) - 1)
    elif line.startsWith("$ cd"):
        dir = line.split("$ cd ")[^1]
        currentDirs.add(dir)
        ls = false
    elif line == "$ ls" and not dirs.hasKey(dir):
        ls = true
    elif line == "$ ls" and dirs.hasKey(dir):
        ls = false
    elif line.startsWith(regex) and ls:
        let size = parseInt(line.split(" ")[0])
        for i in 0..<len(currentDirs):
            let path = currentDirs[0 .. i].join("/")
            if not dirs.hasKey(path):
                dirs[path] = 0
            dirs[path] += size

var total: int
for v in dirs.values:
    if v <= 100000:
        total += v

echo total