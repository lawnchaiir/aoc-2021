package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func exceptWith(s, remove string) string {
	return strings.Map(func(r rune) rune {
		if strings.ContainsRune(remove, r) {
			return -1
		}
		return r
	}, s)
}

func exactMatch(a, b string) bool {
	var sortingArr []rune
	sortFunc := func(i, j int) bool {
		return sortingArr[i] < sortingArr[j]
	}
	sortingArr = []rune(a)
	sort.Slice(sortingArr, sortFunc)
	a = string(sortingArr)
	sortingArr = []rune(b)
	sort.Slice(sortingArr, sortFunc)
	b = string(sortingArr)
	return a == b
}

type SevenSegment struct {
	input  []string
	output []string

	zero  string
	one   string
	two   string
	three string
	four  string
	five  string
	six   string // twaannnng
	seven string
	eight string
	nine  string

	topChar    string
	bottomChar string
	bottomLeft string
}

func (display *SevenSegment) findTopChar() {
	display.topChar = exceptWith(display.seven, display.one)
}

func (display *SevenSegment) findBottomLeft() {
	display.bottomLeft = exceptWith(display.eight, display.nine)
}

// 2,3,5
func (display *SevenSegment) processFiveLengthCode(s string) {
	except := exceptWith(s, display.four)
	if len(except) == 3 {
		display.two = s
	} else if len(display.bottomChar) == 0 {
		display.bottomChar = exceptWith(except, string(display.topChar))
	}
}

// 0 6,9
func (display *SevenSegment) processSixLengthCode(s string) {
	if len(display.nine) != 0 {
		return
	}
	except := exceptWith(s, display.four)
	if len(except) == 2 {
		display.nine = s
	}
}

func (display *SevenSegment) processSecondRoundCodes() {
	for _, s := range display.input {
		switch len(s) {
		case 5:
			display.processFiveLengthCode(s)
		case 6:
			display.processSixLengthCode(s)
		}
	}
}

func (display *SevenSegment) processRemaining() {
	middleChar := exceptWith(display.two, display.seven)
	middleChar = exceptWith(middleChar, display.bottomLeft)
	middleChar = exceptWith(middleChar, display.bottomChar)

	display.zero = exceptWith(display.eight, middleChar)

	bottomRight := exceptWith(display.one, display.two)
	bigC := exceptWith(display.zero, display.one)
	display.six = bigC + middleChar + bottomRight
	display.five = exceptWith(display.six, display.bottomLeft)

	display.three = display.seven + middleChar + display.bottomChar
}

func (display *SevenSegment) solveOutput() int {
	values := []string{
		display.zero,
		display.one,
		display.two,
		display.three,
		display.four,
		display.five,
		display.six,
		display.seven,
		display.eight,
		display.nine,
	}
	currMagnitude := 1000
	ret := 0
	for _, ouputVal := range display.output {
		for idx, v := range values {
			if exactMatch(ouputVal, v) {
				ret += currMagnitude * idx
				currMagnitude /= 10
				continue
			}
		}
	}
	return ret
}

func (display *SevenSegment) processGuaranteedCodes() {
	for _, s := range display.input {
		switch len(s) {
		case 2:
			display.one = s
		case 3:
			display.seven = s
		case 4:
			display.four = s
		case 7:
			display.eight = s
		}
	}
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scan := bufio.NewScanner(file)

	sum := 0

	for scan.Scan() {

		var display SevenSegment

		line := scan.Text()
		splitLine := strings.Split(line, " | ")
		display.input = strings.Split(splitLine[0], " ")
		display.output = strings.Split(splitLine[1], " ")

		display.processGuaranteedCodes()
		display.findTopChar()
		display.processSecondRoundCodes()
		display.findBottomLeft()
		display.processRemaining()

		solution := display.solveOutput()
		sum += solution
	}
	fmt.Println(sum)
}
