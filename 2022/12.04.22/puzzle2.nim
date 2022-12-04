import std/strutils

let input = splitLines(readFile("input.txt"))

proc contain(line: string): bool =
    var nums =  split(line, {'-',','})
    var a = parseInt(nums[0]) <= parseInt(nums[2]) and parseInt(nums[1]) >= parseInt(nums[2])
    var b = parseInt(nums[2]) <= parseInt(nums[0]) and parseInt(nums[3]) >= parseInt(nums[0])
    return a or b

var ct: int
for line in input:
    if contain(line):
        ct+=1

echo ct
