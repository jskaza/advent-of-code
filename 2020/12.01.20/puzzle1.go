package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	sli := InputToSlice("input.txt")
	l := len(sli)

	for i := 0; i < l-1; i++ {
		a := sli[i]
		for j := i + 1; j < l; j++ {
			b := sli[j]
			sum := a + b
			switch sum {
			case 2020:
				fmt.Println(a * b)
				return
			default:
				continue
			}
		}
	}
}

func InputToSlice(f string) []int {
	file, err := os.Open(f)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	ints := make([]int, 0)

	for sc.Scan() {
		num, _ := strconv.Atoi(sc.Text())
		ints = append(ints, num)
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	return ints
}
