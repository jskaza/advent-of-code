import sequtils
import sets

let input = readFile("input.txt")

for i in countup(13,len(input) - 14):
    let marker = input[i .. i+13].toSeq()
    let markerSet = toHashSet(marker)
    if len(marker) == len(markerSet):
        echo i+14
        break