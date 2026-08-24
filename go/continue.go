package main

import "fmt"

func main() {
	var i int = 10
	for i < 20 {
		if i == 15 {
			i++
			continue
		}
		fmt.Println(i)
		i++
	}
}
