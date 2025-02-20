package vehicle

import "strategy/pkg/drive"

type Bike struct {
	*drive.SlowDrive
}

func (b Bike) NoOfWheel() int {
	return 2
}

func newBike(d *drive.SlowDrive) *Bike {
	return &Bike{d}
}
