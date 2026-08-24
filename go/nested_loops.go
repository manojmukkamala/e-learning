package main

import "fmt"

func main() {
	var min, max int = 2, 4
	var up_to int = 10
	fmt.Printf("Tables will be printed from %d to %d using multiplication factor from 1 to %d\n", min, max, up_to)
	for t := min; t <= max; t++ {
		for i := 1; i <= up_to; i++ {
			fmt.Printf("%d * %d = %d \n", t, i, t*i)
		}
	}
}
