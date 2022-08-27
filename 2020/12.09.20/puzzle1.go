package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sli := readInts("input.txt")
	for i := range sli {
		toCheck := sli[i : i+25]
		target := sli[i+25]
		if !twoSum(toCheck, target) {
			fmt.Println(target)
			return
		}
	}
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

func twoSum(array []int, target int) bool {
	seenNums := map[int]int{}
	for i, num := range array {
		potentialMatch := target - num
		if _, found := seenNums[potentialMatch]; found {
			return true
		}
		seenNums[num] = i
	}
	return false
}
