package drive

import "fmt"

type SlowDrive struct{}

func (f SlowDrive) Drive() {
	fmt.Println("slow drive")
}
