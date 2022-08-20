package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	data, cols, rows := ReadInput("input.txt")
	results := map[string]int{
		"test1": 0,
		"test2": 0,
		"test3": 0,
		"test4": 0,
		"test5": 0}

	for i := 1; i < rows; i++ {
		if CheckTree(1, i, cols, data[i]) {
			results["test1"]++
		}
		if CheckTree(3, i, cols, data[i]) {
			results["test2"]++
		}
		if CheckTree(5, i, cols, data[i]) {
			results["test3"]++
		}
		if CheckTree(7, i, cols, data[i]) {
			results["test4"]++
		}
	}
	for i := 2; i < rows; i = i + 2 {
		if CheckTreeSkip(1, i, cols, data[i]) {
			results["test5"]++
		}
	}

	res := 1
	for _, val := range results {
		res = res * val
	}

	fmt.Println(res)
}

func ReadInput(f string) ([][]string, int, int) {
	file, err := os.Open(f)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	var rows [][]string

	for sc.Scan() {
		rows = append(rows, strings.Split(sc.Text(), ""))
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	NCols := len(rows[0])
	NRows := len(rows)

	return rows, NCols, NRows
}

func CheckTree(step, row, l int, data []string) bool {
	mod := (row*step + 1) % l
	if mod == 0 {
		return data[l-1] == "#"
	} else {
		return data[mod-1] == "#"
	}
}

func CheckTreeSkip(step, row, l int, data []string) bool {
	mod := ((row/2)*step + 1) % l
	if mod == 0 {
		return data[l-1] == "#"
	} else {
		return data[mod-1] == "#"
	}

}
