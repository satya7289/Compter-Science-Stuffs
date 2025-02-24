package box

type Ladder struct {
	Start *Coordinate
	End   *Coordinate
}

func NewLadder(start, end *Coordinate) *Ladder {
	return &Ladder{Start: start, End: end}
}
