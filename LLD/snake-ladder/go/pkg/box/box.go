package box

import "fmt"

type Box struct {
	size      int
	c         []*Coordinate
	snakeMap  map[*Coordinate]*Snake
	ladderMap map[*Coordinate]*Ladder
}

func NewBox(size int) *Box {
	c := make([]*Coordinate, 0)
	sno := 1
	odd := false
	for i := 0; i < size; i++ {
		if odd {
			for j := 0; j < size; j++ {
				c = append(c, NewCoordinate(i, j, sno))
				sno++
			}
		} else {
			for j := size - 1; j >= 0; j-- {
				c = append(c, NewCoordinate(i, j, sno))
				sno++
			}
		}
		odd = !odd
	}
	return &Box{
		c:         c,
		size:      size,
		snakeMap:  make(map[*Coordinate]*Snake),
		ladderMap: make(map[*Coordinate]*Ladder),
	}
}

func (b *Box) AddSnake(startSno, endSno int) error {
	it := NewBoxIterator(b.c)
	if !it.HasNext(startSno) {
		return fmt.Errorf("no startSNo found")
	}
	startC := it.GetNext(startSno)

	it2 := NewBoxIterator(b.c)
	if !it2.HasNext(endSno) {
		return fmt.Errorf("no endSno found")
	}
	endC := it2.GetNext(endSno)
	snake := NewSnake(startC, endC)
	b.snakeMap[startC] = snake
	return nil
}

func (b *Box) AddLadder(startSno, endSno int) error {
	it := NewBoxIterator(b.c)
	if !it.HasNext(startSno) {
		return fmt.Errorf("no startSNo found")
	}
	startC := it.GetNext(startSno)

	it2 := NewBoxIterator(b.c)
	if !it2.HasNext(endSno) {
		return fmt.Errorf("no endSno found")
	}
	endC := it2.GetNext(endSno)
	ladder := NewLadder(startC, endC)
	b.ladderMap[startC] = ladder
	return nil
}

func (b *Box) CheckSnake(cor *Coordinate) (*Snake, bool) {
	s, ok := b.snakeMap[cor]
	return s, ok
}

func (b *Box) CheckLadder(cor *Coordinate) (*Ladder, bool) {
	l, ok := b.ladderMap[cor]
	return l, ok
}

func (b *Box) GetCoordinates() []*Coordinate {
	return b.c
}
