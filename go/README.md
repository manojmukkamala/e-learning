# Go Basics

Small standalone Go programs covering core language syntax: variables,
data types, decision making, loops, break/continue, nested loops, and
functions.

Each file is a complete program in its own `main()` — they are meant to be
read one at a time, not built together.

## How to work through it

Requires the [Go toolchain](https://go.dev/dl/) (any recent 1.x version).

Run each program individually:

```sh
go run variables.go
go run data_types.go
go run decision_making.go
go run loops.go
go run break.go
go run continue.go
go run nested_loops.go
go run functions.go
```

Suggested order: `variables.go` → `data_types.go` → `decision_making.go` →
`loops.go` → `break.go` → `continue.go` → `nested_loops.go` → `functions.go`.

No external dependencies; standard library (`fmt`) only.
