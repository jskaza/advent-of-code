package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	bagMap, _ := bagMap("input.txt")
	fmt.Println(countBags(bagMap, "shiny gold"))
}

type innerBag struct {
	color string
	count int
}

func bagMap(path string) (map[string][]innerBag, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	bags := make(map[string][]innerBag, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " bags contain ")
		bag := line[0]
		contains := line[1]
		bags[bag] = parseBags(contains)
	}

	return bags, nil
}

func parseBags(s string) []innerBag {
	bagMap := make([]innerBag, 0)
	switch s {
	case "no other bags.":
		return bagMap
	default:
		bags := strings.Split(s, ", ")
		for _, b := range bags {
			split := strings.Split(b, " ")
			numText := split[0]
			num, _ := strconv.Atoi(numText)
			color := split[1] + " " + split[2]
			bagMap = append(bagMap, innerBag{color: color, count: num})
		}
	}
	return bagMap
}

// recursion, my favorite :/
func countBags(bagMap map[string][]innerBag, bag string) int {
	ct := 0
	outerBag := bagMap[bag]
	if len(outerBag) == 0 {
		return ct
	} else {
		for _, innerBag := range outerBag {
			ct += innerBag.count
			bagsInInnerBag := countBags(bagMap, innerBag.color)
			ct += bagsInInnerBag * innerBag.count
		}
	}
	return ct
}
