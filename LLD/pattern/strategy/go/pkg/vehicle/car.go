package vehicle

import "strategy/pkg/drive"

type Car struct {
	*drive.FastDrive
}

func (b Car) NoOfWheel() int {
	return 4
}

func newCar(d *drive.FastDrive) *Car {
	return &Car{d}
}
