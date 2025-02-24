package floor

import (
	"parkingalot/pkg/vehicle"
	"time"
)

type SpotName string

const (
	Large    SpotName = "large"
	Small    SpotName = "small"
	Electric SpotName = "electric"
)

type Ispot interface {
	SpotId() string
	GetSpotName() SpotName
	GetParkedVehicle() vehicle.IVehicle
	Occupied() bool
	ParkVehicle(vehicle.IVehicle) bool
	UnParkVehicle()
}

func NewSpot(n SpotName, id string) Ispot {
	switch n {
	case Large:
		return &LargeSpot{id: id}
	case Small:
		return &SmallSpot{id: id}
	case Electric:
		return &ElectricSpot{id: id}
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
	l.v.SetExitTime(time.Now())
	l.v = nil
}
func (l *LargeSpot) GetSpotName() SpotName              { return Large }
func (l *LargeSpot) GetParkedVehicle() vehicle.IVehicle { return l.v }

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
func (l *SmallSpot) GetSpotName() SpotName              { return Small }
func (l *SmallSpot) GetParkedVehicle() vehicle.IVehicle { return l.v }

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
func (l *ElectricSpot) GetSpotName() SpotName              { return Electric }
func (l *ElectricSpot) GetParkedVehicle() vehicle.IVehicle { return l.v }
