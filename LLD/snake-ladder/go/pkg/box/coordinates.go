package box

import "fmt"

type Coordinate struct {
	Sno int
	X   int
	Y   int
}

func NewCoordinate(x, y, sno int) *Coordinate {
	return &Coordinate{X: x, Y: y, Sno: sno}
}

func (c *Coordinate) String() string {
	return fmt.Sprintf("%v(%v,%v)", c.Sno, c.X, c.Y)
}
