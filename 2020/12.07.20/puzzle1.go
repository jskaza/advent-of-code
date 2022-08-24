package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	bagsMap, _ := BagMap("input.txt")
	finalBags := HasColor("shiny gold", bagsMap)
	ok := true
	for ok == true {
		toAdd := make([]string, 0)
		for _, bag := range finalBags {
			for _, v := range HasColor(bag, bagsMap) {
				if !Contains(finalBags, v) && !Contains(toAdd, v) {
					toAdd = append(toAdd, v)
				}
			}
		}
		if len(toAdd) == 0 {
			ok = false
			break
		} else {
			for _, v := range toAdd {
				finalBags = append(finalBags, v)
			}
		}
	}
	fmt.Println(len(finalBags))
}

func BagMap(path string) (map[string]map[string]int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	bags := make(map[string]map[string]int, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " bags contain ")
		bag := line[0]
		contains := line[1]
		bags[bag] = ParseBags(contains)
	}

	return bags, nil
}

func ParseBags(s string) map[string]int {
	bag_map := make(map[string]int, 0)
	switch s {
	case "no other bags.":
		return bag_map
	default:
		bags := strings.Split(s, ", ")
		for _, b := range bags {
			split := strings.Split(b, " ")
			num_text := split[0]
			num, _ := strconv.Atoi(num_text)
			bag := split[1] + " " + split[2]
			bag_map[bag] = num
		}
	}
	return bag_map
}

func HasColor(color string, colorMap map[string]map[string]int) []string {
	bags := make([]string, 0)
	for bag, v := range colorMap {
		keys := make([]string, len(v))
		i := 0
		for k := range v {
			keys[i] = k
			i++
		}
		if Contains(keys, color) {
			bags = append(bags, bag)
		}
	}
	return bags
}

func Contains[T comparable](s []T, e T) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}
	return false
}
