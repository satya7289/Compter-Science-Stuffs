package floor

import (
	"fmt"
	"parkingalot/pkg/vehicle"
)

type FloorNumber int

type IFloor interface {
	AddSpot(Ispot)
	AllSpot() []Ispot
	AvaliableSpot(vehicle.IVehicle) (Ispot, bool)
	AddDoor(DoorType, IDoor)
	EntryDoorList() []IDoor
	ExitDoorList() []IDoor
	Display()
}

func NewFloor(id int, entryExitDoor int, sMap map[SpotName]int) IFloor {
	f := &Floor{
		id:         id,
		entryDoors: make([]IDoor, 0),
		exitDoors:  make([]IDoor, 0),
	}
	for i := 0; i < entryExitDoor; i++ {
		f.AddDoor(Entry, NewDoor(Entry))
		f.AddDoor(Exit, NewDoor(Exit))
	}
	for spotName, count := range sMap {
		for i := 0; i < count; i++ {
			f.AddSpot(NewSpot(spotName))
		}
	}

	return f
}

type Floor struct {
	id         int
	entryDoors []IDoor
	exitDoors  []IDoor
	spots      []Ispot
}

// AddDoor implements IFloor.
func (f *Floor) AddDoor(t DoorType, d IDoor) {
	if t == Entry {
		f.entryDoors = append(f.entryDoors, d)
		return
	}
	f.exitDoors = append(f.exitDoors, d)
}

// AddSpot implements IFloor.
func (f *Floor) AddSpot(s Ispot) {
	f.spots = append(f.spots, s)
}

// AllSpot implements IFloor.
func (f *Floor) AllSpot() []Ispot {
	return f.spots
}

// AvaliableSpot implements IFloor.
func (f *Floor) AvaliableSpot(v vehicle.IVehicle) (Ispot, bool) {
	for _, s := range f.spots {
		if !s.Occupied() {
			return s, true
		}
	}
	return nil, false
}

// Display implements IFloor.
func (f *Floor) Display() {
	fmt.Println("_____________________")
	fmt.Println("Floor No: ", f.id)

	fmt.Println("spot list")
	for _, s := range f.spots {
		fmt.Println("spot no -> ", s.SpotId(), "| occupied: ", s.Occupied())
	}

	fmt.Println("# Entry door: ", len(f.entryDoors))
	fmt.Println("# Exit door: ", len(f.exitDoors))

	fmt.Println("_____________________")
}

// EntryDoorList implements IFloor.
func (f *Floor) EntryDoorList() []IDoor {
	return f.entryDoors
}

// ExitDoorList implements IFloor.
func (f *Floor) ExitDoorList() []IDoor {
	return f.exitDoors
}
