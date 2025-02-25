package game

import (
	"errors"
	"fmt"
)

type IBox interface {
	CheckForWinner(IPlayer) bool
	SetPlayer(IPlayer, int, int) error
	Display()
}

func NewBox(n int) IBox {
	pos := make([][]Ipiece, n)
	for i := range pos {
		pos[i] = make([]Ipiece, n)
	}
	return &Box{
		Position: pos,
	}
}

type Box struct {
	Position [][]Ipiece
}

func (b *Box) CheckForWinner(p IPlayer) bool {
	r, c, d := 0, 0, 0
	for i := range len(b.Position) {
		for j := range len(b.Position) {
			if b.Position[i][j] == p.GetPiece() {
				r++
			}
			if b.Position[j][i] == p.GetPiece() {
				c++
			}
		}
		if b.Position[i][i] == p.GetPiece() {
			d++
		}
	}
	return r == len(b.Position) || c == len(b.Position) || d == len(b.Position)
}

func (b *Box) SetPlayer(p IPlayer, x, y int) error {
	if x < 0 || y < 0 || x >= len(b.Position) || y >= len(b.Position) {
		return errors.New("invalid position")
	}

	if b.Position[x][y] != nil {
		return errors.New("position already filled")
	}

	b.Position[x][y] = p.GetPiece()
	return nil
}

func (b *Box) Display() {
	for i, row := range b.Position {
		for j, col := range row {
			fmt.Printf("%-10v(%d,%d) |", col, i, j)
		}
		fmt.Println()
	}
}
