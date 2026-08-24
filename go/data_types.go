package main

import "fmt"

func main() {
	var x float32 = 10.1
	fmt.Println(x)
	fmt.Printf("x is of type %T\n", x)

	var a, b, c = 1, 2, 3
	fmt.Println(a, b, c)

	y, z := 10, 20
	fmt.Println(y, z)

	const A = 10
	// A := 11 //gives error : cannot assign to A
	fmt.Println(A)
}
