package game

import (
	"fmt"
	"snakeladder/pkg/box"

	"math/rand"
)

func StartGame() {
	b := box.NewBox(10)

	// add snakes
	b.AddSnake(95, 10)
	b.AddSnake(83, 2)
	b.AddSnake(50, 2)

	// add ladder
	b.AddLadder(3, 80)
	b.AddLadder(21, 68)
	b.AddLadder(33, 99)

	// player
	playerList := make([]*Player, 0)
	playerList = append(playerList, NewPlayer("satya", box.NewBoxIterator(b.GetCoordinates())), NewPlayer("aman", box.NewBoxIterator(b.GetCoordinates())))

	for {
		p := playerList[0]
		playerList = append(playerList, p)
		playerList = playerList[1:]

		fmt.Printf(`
Player %v is playing. Current position: %v;
Enter any key to roll dice:
`, p.Name, p.Iterator.Current().String())

		var x rune
		fmt.Scan(&x)
		n := 1 + rand.Intn(6-1+1)

		fmt.Println("Dice output: ", n)
		if ok := p.Iterator.HasNext(n); !ok {
			fmt.Println("No futher excceded")
		} else {
			fmt.Println("Moved to Position: ", p.Iterator.GetNext(n).String())
		}

		if s, ok := b.CheckSnake(p.Iterator.Current()); ok {
			p.Iterator.SetIdxByCoordinate(s.End)
			fmt.Println("Snake bite, Updated Position: ", p.Iterator.Current().String())
		} else if s, ok := b.CheckLadder(p.Iterator.Current()); ok {
			p.Iterator.SetIdxByCoordinate(s.End)
			fmt.Println("Ladder found, Updated Position: ", p.Iterator.Current().String())
		}

		if p.Iterator.IsLast() {
			fmt.Printf("Player %v win the game", p.Name)
			return
		}
	}
}
