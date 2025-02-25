package box

type BoxIterator interface {
	HasNext(int) bool
	GetNext(int) *Coordinate
	Current() *Coordinate
	SetIdxByCoordinate(*Coordinate)
	IsLast() bool
}

func NewBoxIterator(c []*Coordinate) BoxIterator {
	return &iterator{c: c}
}

type iterator struct {
	idx int
	c   []*Coordinate
}

func (it *iterator) HasNext(n int) bool {
	return it.idx+n < len(it.c)
}

func (it *iterator) GetNext(n int) *Coordinate {
	it.idx += n
	return it.c[it.idx-1]
}

func (it *iterator) IsLast() bool {
	return it.idx == len(it.c)
}

func (it *iterator) Current() *Coordinate {
	if it.idx == 0 {
		return nil
	}
	return it.c[it.idx-1]
}

func (it *iterator) SetIdxByCoordinate(c *Coordinate) {
	for i, _c := range it.c {
		if _c == c {
			it.idx = i
		}
	}
}
