package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	seats := make([]int, 0)
	for scanner.Scan() {
		seat := Seat{scanner.Text(), 0, 127, 0, 7}
		id := seat.SeatFinder()
		seats = append(seats, id)
	}

	sort.Slice(seats, func(i, j int) bool {
		return seats[i] < seats[j]
	})

	for i, v := range seats {
		if seats[i+1] != v+1 {
			fmt.Printf("It's seat ID %v!", v+1)
			return
		}
	}
}

type Seat struct {
	seat    string
	rowMin  float64
	rowMax  float64
	seatMin float64
	seatMax float64
}

func (s Seat) SeatFinder() int {
	for _, j := range s.seat[:7] {
		s.UpdateRowRange(s.RowMidpoint(), string(j))
	}
	for _, j := range s.seat[7:] {
		s.UpdateSeatRange(s.SeatMidpoint(), string(j))
	}
	return int(s.rowMax*8 + s.seatMax)
}

func (s Seat) RowMidpoint() float64 {
	return (s.rowMin + s.rowMax) / 2
}

func (s Seat) SeatMidpoint() float64 {
	return (s.seatMin + s.seatMax) / 2
}

func (s *Seat) UpdateRowRange(midpoint float64, section string) {
	switch section {
	case "F":
		s.rowMax = math.Floor(midpoint)
	case "B":
		s.rowMin = math.Ceil(midpoint)
	default:
		return
	}
}

func (s *Seat) UpdateSeatRange(midpoint float64, section string) {
	switch section {
	case "L":
		s.seatMax = math.Floor(midpoint)
	case "R":
		s.seatMin = math.Ceil(midpoint)
	default:
		return
	}
}
