package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

type Point struct {
	x int
	y int
}

type Line struct {
	start Point
	end   Point
}

func (line Line) isDiagonal() bool {
	return line.start.x != line.end.x &&
		line.start.y != line.end.y

}

func interpolate(start, curr, end int) (int, bool) {
	if start < end {
		curr++
		if curr > end {
			return curr, false
		}
	} else if start > end {
		curr--
		if curr < end {
			return curr, false
		}
	} else {
		return curr, false
	}

	return curr, true
}

func loadInput() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scan := bufio.NewScanner(file)

	for scan.Scan() {
		line := scan.Text()

		matches := p.FindStringSubmatch(line)

		x1, _ := strconv.ParseInt(matches[1], 10, 32)
		y1, _ := strconv.ParseInt(matches[2], 10, 32)

		start := Point{int(x1), int(y1)}

		x2, _ := strconv.ParseInt(matches[3], 10, 32)
		y2, _ := strconv.ParseInt(matches[4], 10, 32)

		end := Point{int(x2), int(y2)}

		l := Line{start, end}

		Lines = append(Lines, l)
	}
}

var (
	p           = regexp.MustCompile(`(\d+),(\d+) -> (\d+),(\d+)`)
	Lines       []Line
	pointCounts map[Point]int = make(map[Point]int)
)

func main() {
	loadInput()

	for _, line := range Lines {
		/*if line.isDiagonal() {
			continue
		}*/

		iterX, iterY := true, true
		x := line.start.x
		y := line.start.y
		for iterX || iterY {
			p := Point{x, y}
			if count, ok := pointCounts[p]; ok {
				pointCounts[p] = count + 1
			} else {
				pointCounts[p] = 1
			}
			x, iterX = interpolate(line.start.x, x, line.end.x)
			y, iterY = interpolate(line.start.y, y, line.end.y)
		}
	}

	overlapCount := 0
	for _, ct := range pointCounts {
		if ct > 1 {
			overlapCount++
		}
	}

	fmt.Println("Overlaps: ", overlapCount)
}
