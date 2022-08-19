package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	pos1, pos2, letters, passwords := CreateData("input.txt")
	valid := 0
	for i := range pos1 {
		if CheckValidity(passwords[i], letters[i], pos1[i], pos2[i]) {
			valid++
		}
	}
	fmt.Println(valid)
}

func CreateData(f string) ([]int, []int, []string, []string) {
	file, err := os.Open(f)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	pos1 := make([]int, 0)
	pos2 := make([]int, 0)
	letters := make([]string, 0)
	passwords := make([]string, 0)

	for sc.Scan() {
		line := ParseLine(sc.Text())
		p1, _ := strconv.Atoi(line[0])
		p2, _ := strconv.Atoi(line[1])
		pos1 = append(pos1, p1)
		pos2 = append(pos2, p2)
		letters = append(letters, line[2])
		passwords = append(passwords, line[3])
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	return pos1, pos2, letters, passwords

}

func CheckValidity(s, letter string, p1, p2 int) bool {
	x := string(s[p1-1]) == letter
	y := string(s[p2-1]) == letter
	return (x || y) && !(x && y)
}

func ParseLine(line string) []string {
	p := regexp.MustCompile(":|-")
	cleaned := p.ReplaceAllString(line, " ")
	return strings.Fields(cleaned)
}
