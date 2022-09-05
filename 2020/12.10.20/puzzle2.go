package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	c := make(chan int)
	var pathsMap = map[int]int{
		// this map represents the number of permutations given a group size
		1: 1,
		2: 1,
		3: 2,
		4: 4,
		5: 7,
	}
	sli := readInts("input.txt")
	groups := makeGroups(sli)
	wg.Add(len(groups) + 1)
	for i := 0; i < len(groups); i++ {
		go processGroup(groups[i], pathsMap, c, &wg)
	}
	go cumProd(c, len(groups), &wg)
	wg.Wait()
}

func readInts(path string) []int {
	file, _ := os.Open(path)
	defer file.Close()

	var ints = []int{0} // prepend 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		ints = append(ints, i)
	}

	sort.Ints(ints)
	ints = append(ints, ints[len(ints)-1]+3) // append max+3
	return ints
}

func makeGroups(sli []int) [][]int {
	// pull out each chunk of consecutive numbers
	groups := make([][]int, 0)
	groups = append(groups, []int{sli[0]})
	for i := 1; i < len(sli); i++ {
		switch sli[i] - sli[i-1] {
		case 1:
			groups[len(groups)-1] = append(groups[len(groups)-1], sli[i])
		default:
			groups = append(groups, []int{sli[i]})
		}
	}
	return groups
}

func processGroup(group []int, pathsMap map[int]int, c chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	// determine the length of the chunk
	// grab n permutations for chunk using lookup
	c <- pathsMap[len(group)]
}

func cumProd(c chan int, nGroups int, wg *sync.WaitGroup) {
	defer wg.Done()
	var res int = 1
	ct := 0
	for i := range c {
		res = res * i
		ct++
		if ct == nGroups {
			close(c)
		}
	}
	fmt.Println(res)
}
