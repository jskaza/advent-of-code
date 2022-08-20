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
	res := 0
	for i := 1; i < rows; i++ {
		if CheckTree(3, i, cols, data[i]) {
			res++
		}
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
