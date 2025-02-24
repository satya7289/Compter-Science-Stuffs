package box

type Snake struct {
	Start *Coordinate
	End   *Coordinate
}

func NewSnake(start, end *Coordinate) *Snake {
	return &Snake{Start: start, End: end}
}
