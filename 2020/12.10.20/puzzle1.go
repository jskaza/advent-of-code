package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	sli := readInts("input.txt")
	m := differencesMap(sli)
	fmt.Println(m[1] * m[3])

}

func readInts(path string) []int {
	file, _ := os.Open(path)
	defer file.Close()

	var ints []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		ints = append(ints, i)
	}

	return ints
}

func builtInAdapter(sli []int) int {
	max := sli[0]
	for i := 1; i < len(sli); i++ {
		if sli[i] > max {
			max = sli[i]
		}
	}
	return max + 3
}

func differencesMap(sli []int) map[int]int {
	var res = map[int]int{1: 0, 3: 1} //initialize 3 to 1 bc of last step
	sort.Ints(sli)
	res[sli[0]]++
	for i := 0; i < len(sli)-1; i++ {
		switch sli[i+1] - sli[i] {
		case 1:
			res[1]++
		case 3:
			res[3]++
		}
	}
	return res
}
