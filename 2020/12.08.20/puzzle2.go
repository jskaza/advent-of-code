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
	for i := range instructions {

		if instructions[i].instr == "jmp" || instructions[i].instr == "nop" {
			newInstructions := make([]instruction, len(instructions))
			copy(newInstructions, instructions)
			newInstructions[i] = newInstructions[i].swap()
			term, acc := checkTermination(newInstructions)
			if term {
				fmt.Println(acc)
				return
			}
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

func (i instruction) swap() instruction {
	switch i.instr {
	case "nop":
		i.instr = "jmp"
	case "jmp":
		i.instr = "nop"
	}
	return i
}

func checkTermination(instructions []instruction) (bool, int) {
	i := 0
	acc := 0
	for {
		if i == len(instructions) {
			return true, acc
		} else if instructions[i].visited {
			return false, acc
		} else {
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
}
