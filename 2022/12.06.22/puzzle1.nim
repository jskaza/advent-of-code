import sequtils
import sets

let input = readFile("input.txt")

for i in countup(3,len(input) - 4):
    let marker = input[i .. i+3].toSeq()
    let markerSet = toHashSet(marker)
    if len(marker) == len(markerSet):
        echo i+4
        break