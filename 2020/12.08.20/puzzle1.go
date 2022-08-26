package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	instructions := readData("input.txt")
	acc := 0
	i := 0
	for {
		if instructions[i].visited {
			fmt.Println(acc)
			return
		}
		instructions[i].visited = true
		switch instructions[i].instr {
		case "acc":
			acc += instructions[i].val
			i++
		case "jmp":
			i += instructions[i].val
		default:
			i++
		}
	}
}

type instruction struct {
	instr   string
	val     int
	visited bool
}

func readData(path string) []instruction {
	file, _ := os.Open(path)
	defer file.Close()

	instructions := make([]instruction, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		instructions = append(instructions, parseLine(scanner.Text()))
	}

	return instructions
}

func parseLine(s string) instruction {
	fields := strings.Fields(s)
	val, _ := strconv.Atoi(fields[1])
	return instruction{instr: fields[0], val: val}
}
