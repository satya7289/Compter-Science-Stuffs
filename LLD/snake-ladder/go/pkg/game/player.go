package game

import "snakeladder/pkg/box"

type Player struct {
	Name     string
	Iterator box.BoxIterator
}

func NewPlayer(n string, it box.BoxIterator) *Player {
	return &Player{Name: n, Iterator: it}
}
