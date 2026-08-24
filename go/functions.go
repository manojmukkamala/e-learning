package main

import "fmt"

func main() {
	var x, y int = 10, 20
	res := max_of_two(x, y)
	fmt.Printf("%d is the large value \n", res)
}

func max_of_two(x int, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
