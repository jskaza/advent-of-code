package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sli := readInts("input.txt")
	invalidNum, err := findCorrupt(sli, 25)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(findSumToTarget(sli, invalidNum))
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

func findCorrupt(sli []int, preamble int) (int, error) {
	for i := range sli {
		toCheck := sli[i : i+preamble]
		target := sli[i+preamble]
		if !twoSum(toCheck, target) {
			return target, nil
		}
	}
	return -1, errors.New("couldn't find corrupt number")
}

func sumToTarget(sli []int, i, target int) (bool, []int) {
	sum := 0
	start := i
	for sum < target {
		sum += sli[i]
		if sum == target {
			return true, sli[start : i+1]
		}
		i++
	}
	return false, []int{}
}

func findSumToTarget(sli []int, target int) int {
	for i := range sli {
		check, subSli := sumToTarget(sli, i, target)
		if check {
			return minIntSlice(subSli) + maxIntSlice(subSli)
		}
	}
	return 0
}

func minIntSlice(v []int) int {
	var m int
	for i, e := range v {
		if i == 0 || e < m {
			m = e
		}
	}
	return m
}

func maxIntSlice(v []int) int {
	var m int
	for i, e := range v {
		if i == 0 || e > m {
			m = e
		}
	}
	return m
}
