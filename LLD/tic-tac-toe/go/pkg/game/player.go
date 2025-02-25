package game

type IPlayer interface {
	play()
	GetPiece() Ipiece
}

func NewPlayer(p Ipiece) IPlayer {
	return &Player{p}
}

type Player struct {
	Piece Ipiece
}

func (p *Player) play()            {}
func (p *Player) GetPiece() Ipiece { return p.Piece }
