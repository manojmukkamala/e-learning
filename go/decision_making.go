package main

import "fmt"

func main() {
	var a int = -10
	fmt.Printf("Value of a: %d\n", a)

	if a == 0 {
		fmt.Println("a is zero")
	} else if a > 0 {
		fmt.Println("a is a positive number")
	} else {
		fmt.Println("a is a negative number")
	}
}
