package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	data, _ := ReadInput("input.txt")
	sum := 0
	for _, s := range data {
		sum = sum + GetUnique(s)
	}
	fmt.Println(sum)
}

func ReadInput(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	lines := make([]string, 1)
	scanner := bufio.NewScanner(file)
	currentLine := 0
	for scanner.Scan() {
		if scanner.Text() == "" {
			lines = append(lines, "")
			currentLine++
		} else {
			lines[currentLine] = lines[currentLine] + scanner.Text()
		}

	}
	return lines, nil
}

func GetUnique(s string) int {
	chars := make(map[rune]bool, 0)
	for _, r := range s {
		if chars[r] {
			continue
		} else {
			chars[r] = true
		}
	}

	return len(chars)
}
