package vehicle

import "time"

type VehicleName string

const (
	Car  VehicleName = "car"
	Bike VehicleName = "bike"
)

var _vechileNames []VehicleName

func init() {
	_vechileNames = []VehicleName{Car, Bike}
}

func GetAllSupportedVehicleName() []VehicleName {
	return _vechileNames
}

type IVehicle interface {
	GetId() string
	GetVehicleName() VehicleName
	GetEntryTime() time.Time
	SetEntryTime(time.Time)
	GetExitTime() time.Time
	SetExitTime(time.Time)
	vehicle()
}

func NewVehicle(n VehicleName, id string) IVehicle {
	switch n {
	case Car:
		return &CarVehicle{id: id}
	case Bike:
		return &BikeVehicle{id: id}
	default:
		panic("unknown vehicle")
	}
}

// car
type CarVehicle struct {
	id                  string
	entryTime, exitTime time.Time
}

func (c *CarVehicle) vehicle()                    {}
func (c *CarVehicle) GetId() string               { return c.id }
func (c *CarVehicle) String() string              { return string(Car) }
func (c *CarVehicle) GetEntryTime() time.Time     { return c.entryTime }
func (c *CarVehicle) SetEntryTime(t time.Time)    { c.entryTime = t }
func (c *CarVehicle) GetExitTime() time.Time      { return c.exitTime }
func (c *CarVehicle) SetExitTime(t time.Time)     { c.exitTime = t }
func (c *CarVehicle) GetVehicleName() VehicleName { return Car }

// bike
type BikeVehicle struct {
	id                  string
	entryTime, exitTime time.Time
}

func (c *BikeVehicle) vehicle()                    {}
func (c *BikeVehicle) GetId() string               { return c.id }
func (c *BikeVehicle) String() string              { return string(Bike) }
func (c *BikeVehicle) GetEntryTime() time.Time     { return c.entryTime }
func (c *BikeVehicle) SetEntryTime(t time.Time)    { c.entryTime = t }
func (c *BikeVehicle) GetExitTime() time.Time      { return c.exitTime }
func (c *BikeVehicle) SetExitTime(t time.Time)     { c.exitTime = t }
func (c *BikeVehicle) GetVehicleName() VehicleName { return Bike }
