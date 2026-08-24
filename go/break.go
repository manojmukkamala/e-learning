package main

import "fmt"

func main() {
	var i int = 10
	for i < 20 {
		fmt.Println(i)
		i++
		if i > 15 {
			break
		}
	}
}
