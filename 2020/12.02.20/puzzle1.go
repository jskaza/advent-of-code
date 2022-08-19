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
	mins, maxes, letters, passwords := CreateData("input.txt")
	valid := 0
	for i := range mins {
		if CheckValidity(passwords[i], letters[i], mins[i], maxes[i]) {
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
	mins := make([]int, 0)
	maxes := make([]int, 0)
	letters := make([]string, 0)
	passwords := make([]string, 0)

	for sc.Scan() {
		line := ParseLine(sc.Text())
		min, _ := strconv.Atoi(line[0])
		max, _ := strconv.Atoi(line[1])
		mins = append(mins, min)
		maxes = append(maxes, max)
		letters = append(letters, line[2])
		passwords = append(passwords, line[3])
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	return mins, maxes, letters, passwords

}

func CheckValidity(s, letter string, min, max int) bool {
	check_min := strings.Count(s, letter) >= min
	check_max := strings.Count(s, letter) <= max
	return check_min && check_max
}

func ParseLine(line string) []string {
	p := regexp.MustCompile(":|-")
	cleaned := p.ReplaceAllString(line, " ")
	return strings.Fields(cleaned)
}
