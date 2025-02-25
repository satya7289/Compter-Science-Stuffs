package game

import "fmt"

func InitGame() {
	box := NewBox(3)
	xPiece, oPiece := NewPiece(X), NewPiece(O)
	p1 := NewPlayer(xPiece)
	p2 := NewPlayer(oPiece)

	queue := make([]IPlayer, 0)
	queue = append(queue, p1, p2)

	for {
		p := queue[0]
		queue = append(queue, p)
		queue = queue[1:]

		fmt.Printf("player %v is playing\n", p.GetPiece())
		box.Display()

	loop:
		var x, y int
		fmt.Print("Choose position: ")
		fmt.Scan(&x, &y)
		if err := box.SetPlayer(p, x, y); err != nil {
			fmt.Printf("Error in setting player position %v\n", err)
			goto loop
		}

		if box.CheckForWinner(p) {
			fmt.Printf("Player %v is winner\n", p.GetPiece())
			return
		}
	}
}
