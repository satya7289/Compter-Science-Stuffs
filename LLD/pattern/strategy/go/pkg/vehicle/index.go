package vehicle

import "strategy/pkg/drive"

type IVehicle interface {
	drive.IDrive
	NoOfWheel() int
}

func NewVehicle(name string, d drive.IDrive) IVehicle {
	switch name {
	case "bike":
		_d, ok := d.(*drive.SlowDrive)
		if !ok {
			panic("drive not a slow drive")
		}
		return newBike(_d)
	case "car":
		_d, ok := d.(*drive.FastDrive)
		if !ok {
			panic("drive not a slow drive")
		}
		return newCar(_d)
	default:
		panic("not implemented name")
	}
}
