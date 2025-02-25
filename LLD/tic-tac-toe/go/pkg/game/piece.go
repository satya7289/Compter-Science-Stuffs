package game

type PieceType string

var (
	X PieceType = "X"
	O PieceType = "O"
)

type Ipiece interface {
	piece()
}

func NewPiece(n PieceType) Ipiece {
	switch n {
	case X:
		return &Xpiece{}
	case O:
		return &Opiece{}
	default:
		panic("unsupported piece type")
	}
}

type Xpiece struct{}

func (*Xpiece) piece()         {}
func (*Xpiece) String() string { return string(X) }

type Opiece struct{}

func (*Opiece) piece()         {}
func (*Opiece) String() string { return string(O) }
