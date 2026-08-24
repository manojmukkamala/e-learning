package main

import "fmt"

func main() {

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
	fmt.Println("hello")

	var a, b int = 10, 15

	for a < b {
		a++
		fmt.Printf("Value of a: %d\n", a)
	}

	var num = [6]int{1, 2, 3, 5}
	for i, x := range num {
		fmt.Printf("Value of x = %d at i = %d \n", x, i)
	}
}
