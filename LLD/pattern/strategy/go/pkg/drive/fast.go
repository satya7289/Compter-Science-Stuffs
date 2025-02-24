package drive

import "fmt"

type FastDrive struct{}

func (f FastDrive) Drive() {
	fmt.Println("fast drive")
}
