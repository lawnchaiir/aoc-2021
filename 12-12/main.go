package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

var (
	nodes map[string]*Node = map[string]*Node{}
)

type Node struct {
	connections []*Node
	smallCave   bool
	name        string
	isStart     bool
	isEnd       bool
}

func hasLower(s string) bool {
	for i := 0; i < len(s); i++ {
		c := s[i]
		if 'a' <= c && c <= 'z' {
			return true
		}
	}
	return false
}

func contains(s []*Node, n *Node) bool {
	for _, o := range s {
		if o == n {
			return true
		}
	}
	return false
}

func (n *Node) Link(other *Node) {
	if !contains(n.connections, other) {
		n.connections = append(n.connections, other)
	}
	if !contains(other.connections, n) {
		other.connections = append(other.connections, n)
	}
}

func main() {
	loadInput()

	// put the large caves first, as they're more likely to have a longer chain that
	// contains other sub-chains
	for _, n := range nodes {
		sort.Slice(n.connections, func(i, j int) bool {
			a := n.connections[i]
			b := n.connections[j]
			return a.name < b.name
		})
	}

	startNode := nodes["start"]
	startNode.isStart = true

	endNode := nodes["end"]
	endNode.isEnd = true

	//var paths [][]*Node

	for _, n := range startNode.connections {
		visitCounts := make(map[*Node]int)
		currNode := n
		for currNode != nil {
			fmt.Println(currNode.name)
			break
		}
	}
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
		dash := strings.Index(line, "-")
		leftNodeId := line[:dash]
		rightNodeId := line[dash+1:]
		var found bool
		var leftNode, rightNode *Node

		if leftNode, found = nodes[leftNodeId]; !found {
			leftNode = &Node{name: leftNodeId, smallCave: hasLower(leftNodeId)}
			nodes[leftNodeId] = leftNode
		}

		if rightNode, found = nodes[rightNodeId]; !found {
			rightNode = &Node{name: rightNodeId, smallCave: hasLower(rightNodeId)}
			nodes[rightNodeId] = rightNode
		}

		leftNode.Link(rightNode)
	}
}
