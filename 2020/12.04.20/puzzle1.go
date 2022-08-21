package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// byr (Birth Year)
// iyr (Issue Year)
// eyr (Expiration Year)
// hgt (Height)
// hcl (Hair Color)
// ecl (Eye Color)
// pid (Passport ID)
// cid (Country ID) // OPTIONAL

func main() {
	data, _ := ReadInput("input.txt")
	required := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	optional := []string{"cid"}
	valid := 0
	for _, d := range data {
		if CheckFields(required, d, optional) {
			valid++
		}
	}
	fmt.Println(valid)
}

func ReadInput(path string) ([][]string, error) {
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
			lines[currentLine] = lines[currentLine] + " " + scanner.Text()
		}

	}

	fields := make([][]string, 0)
	for _, line := range lines {
		f := make([]string, 0)
		for _, pair := range strings.Fields(line) {
			s := strings.Split(pair, ":")
			f = append(f, s[0])
		}
		fields = append(fields, f)
	}

	return fields, scanner.Err()
}

func CheckFields(X, Y, optional []string) bool {
	m := make(map[string]int)
	for _, y := range Y {
		m[y]++
	}

	var res []string
	for _, x := range X {
		if m[x] > 0 {
			m[x]--
			continue
		}
		res = append(res, x)
	}

	for _, j := range res {
		if !Contains(optional, j) {
			return false
		}
	}
	return true
}

func Contains(s []string, str string) bool {
	for _, v := range s {
		if v == str {
			return true
		}
	}

	return false
}
