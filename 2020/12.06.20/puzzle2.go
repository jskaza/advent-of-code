package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	data, _ := ReadInput("input.txt")
	sum := 0
	for _, s := range data {
		sum = sum + CheckAll(s)
	}
	fmt.Println(sum)
}

func ReadInput(path string) ([][]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	lines := make([][]string, 1)
	scanner := bufio.NewScanner(file)
	currentLine := 0
	for scanner.Scan() {
		if scanner.Text() == "" {
			lines = append(lines, make([]string, 0))
			currentLine++
		} else {
			lines[currentLine] = append(lines[currentLine], scanner.Text())
		}

	}
	return lines, nil
}

func CheckAll(arr []string) int {
	baseSeq := arr[0]
	ct := 0
	for _, r := range baseSeq {
		hasRune := 0
		for _, s := range arr {
			if strings.ContainsRune(s, r) {
				hasRune++
			} else {
				break
			}
		}
		if hasRune == len(arr) {
			ct++
		}
	}

	return ct
}
