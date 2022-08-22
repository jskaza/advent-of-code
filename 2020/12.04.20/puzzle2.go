package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// Fields
// byr (Birth Year)
// iyr (Issue Year)
// eyr (Expiration Year)
// hgt (Height)
// hcl (Hair Color)
// ecl (Eye Color)
// pid (Passport ID)
// cid (Country ID) // OPTIONAL

// Data validation
// byr (Birth Year) - four digits; at least 1920 and at most 2002.
// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// pid (Passport ID) - a nine-digit number, including leading zeroes.
// cid (Country ID) - ignored, missing or not.

func main() {
	passports, _ := ReadInput("input.txt")
	required := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	optional := []string{"cid"}
	validEcl := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

	var valid int
	for _, p := range passports {
		fields := GetFields(p)
		if CheckFields(required, fields, optional) {
			var validData int
			for k, v := range p {
				switch k {
				case "byr":
					if len(v) == 4 && Between(v, 1920, 2002) {
						validData++
					}
				case "iyr":
					if len(v) == 4 && Between(v, 2010, 2020) {
						validData++
					}
				case "eyr":
					if len(v) == 4 && Between(v, 2020, 2030) {
						validData++
					}
				case "hgt":
					if CheckHeight(v, 59, 76, 150, 193) {
						validData++
					}
				case "hcl":
					if CheckHairColor(v, "^[a-f0-9]+$") {
						validData++
					}
				case "ecl":
					if CheckEyeCol(v, validEcl) {
						validData++
					}

				case "pid":
					if CheckPassID(v) {
						validData++
					}
				default:
					continue

				}
			}
			if validData == 7 {
				valid++
			}
		}
	}
	fmt.Println(valid)
}

type Passport map[string]string

func ReadInput(path string) ([]Passport, error) {
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

	data := make([]Passport, 0)
	for _, line := range lines {
		p := make(Passport, 0)
		for _, pair := range strings.Fields(line) {
			s := strings.Split(pair, ":")
			p[s[0]] = s[1]
		}
		data = append(data, p)
	}

	return data, scanner.Err()
}

func GetFields(p Passport) []string {
	fields := make([]string, 0)
	for k, _ := range p {
		fields = append(fields, k)
	}
	return fields
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

func Between(s string, lower, upper int) bool {
	parsed, err := strconv.Atoi(s)
	if err != nil {
		return false
	} else {
		return parsed >= lower && parsed <= upper
	}
}

func CheckHeight(s string, lower_in, upper_in, lower_cm, upper_cm int) bool {
	unit := s[len(s)-2:]
	num := s[0 : len(s)-2]
	switch unit {
	case "in":
		return Between(num, lower_in, upper_in)
	case "cm":
		return Between(num, lower_cm, upper_cm)
	default:
		return false
	}
}

func CheckPassID(s string) bool {
	digits := len(s)
	_, err := strconv.Atoi(s)
	if err != nil {
		return false
	} else {
		return digits == 9
	}
}

func CheckHairColor(s, regex string) bool {
	if len(s) != 7 {
		return false
	} else if string(s[0]) != "#" {
		return false
	} else {
		rest := s[1:]
		match, _ := regexp.MatchString(regex, rest)
		return match
	}
}

func CheckEyeCol(s string, valid []string) bool {
	for _, i := range valid {
		if i == s {
			return true
		}
	}
	return false
}
