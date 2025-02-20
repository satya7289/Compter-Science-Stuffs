package floor

import (
	"parkingalot/pkg/vehicle"
	"time"

	"github.com/google/uuid"
)

type SpotName string

const (
	Large    SpotName = "large"
	Small    SpotName = "small"
	Electric SpotName = "electric"
)

type Ispot interface {
	SpotId() string
	Occupied() bool
	ParkVehicle(vehicle.IVehicle) bool
	UnParkVehicle()
}

func NewSpot(n SpotName) Ispot {
	switch n {
	case Large:
		return &LargeSpot{id: uuid.NewString()}
	case Small:
		return &SmallSpot{id: uuid.NewString()}
	case Electric:
		return &ElectricSpot{id: uuid.NewString()}
	default:
		panic("unknown spot name")
	}
}

// large spot
type LargeSpot struct {
	id string
	v  vehicle.IVehicle
}

func (l *LargeSpot) SpotId() string { return l.id }
func (l *LargeSpot) Occupied() bool {
	return l.v != nil
}
func (l *LargeSpot) ParkVehicle(v vehicle.IVehicle) bool {
	if l.v != nil {
		return false
	}
	l.v = v
	v.SetEntryTime(time.Now())
	return true
}
func (l *LargeSpot) UnParkVehicle() {
	l.v = nil
}

// small spot
type SmallSpot struct {
	id string
	v  vehicle.IVehicle
}

func (l *SmallSpot) SpotId() string { return l.id }
func (l *SmallSpot) Occupied() bool {
	return l.v != nil
}
func (l *SmallSpot) ParkVehicle(v vehicle.IVehicle) bool {
	if l.v != nil {
		return false
	}
	l.v = v
	v.SetEntryTime(time.Now())
	return true
}
func (l *SmallSpot) UnParkVehicle() {
	l.v = nil
}

// electric spot
type ElectricSpot struct {
	id string
	v  vehicle.IVehicle
}

func (l *ElectricSpot) SpotId() string { return l.id }
func (l *ElectricSpot) Occupied() bool {
	return l.v != nil
}
func (l *ElectricSpot) ParkVehicle(v vehicle.IVehicle) bool {
	if l.v != nil {
		return false
	}
	l.v = v
	v.SetEntryTime(time.Now())
	return true
}
func (l *ElectricSpot) UnParkVehicle() {
	l.v = nil
}
