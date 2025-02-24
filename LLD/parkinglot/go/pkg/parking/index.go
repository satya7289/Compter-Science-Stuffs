package parking

import (
	"fmt"
	"parkingalot/pkg/floor"
	"parkingalot/pkg/vehicle"
)

var handler = map[int]func(){
	1: checkInHandler,
	2: checkoutHandler,
	3: displayFloor,
}

var (
	floorList      []floor.IFloor
	vehiclePricing map[vehicle.VehicleName]vehicle.Iprice
	vehicleSpot    map[string]floor.Ispot
)

func InitParkinglot() {
	floorList = append(floorList, floor.NewFloor(0, 3, map[floor.SpotName]int{floor.Small: 10, floor.Large: 5, floor.Electric: 2}))
	floorList = append(floorList, floor.NewFloor(1, 3, map[floor.SpotName]int{floor.Small: 10, floor.Large: 5, floor.Electric: 2}))

	vehiclePricing = make(map[vehicle.VehicleName]vehicle.Iprice)
	vehicleSpot = make(map[string]floor.Ispot)
	for _, v := range vehicle.GetAllSupportedVehicleName() {
		switch v {
		case vehicle.Car:
			vehiclePricing[v] = vehicle.NewPrice(vehicle.A)
		case vehicle.Bike:
			vehiclePricing[v] = vehicle.NewPrice(vehicle.B)
		}
	}

	for {
		op := chooseOptions()
		if fn, ok := handler[op]; ok {
			fn()
		} else {
			fmt.Println("Thankyou!!!")
			return
		}
	}
}

func checkInHandler() {
	sno := chooseVehicle()
	vehicleId := enterVehicleNo()
	newVeh := vehicle.NewVehicle(vehicle.GetAllSupportedVehicleName()[sno], vehicleId)

	var spot floor.Ispot
	var ok bool
	var fNo int
	for i, f := range floorList {
		fNo = i
		if spot, ok = f.AvaliableSpot(newVeh); ok {
			fmt.Println("Available Parking for ", newVeh)
			break
		}
	}
	if !ok {
		fmt.Println("Parking not available for ", newVeh)
		return
	}
	spot.ParkVehicle(newVeh)
	vehicleSpot[newVeh.GetId()] = spot
	fmt.Printf("Successfully %v:%v parked on floor: %v, spotId: %v\n", newVeh, newVeh.GetId(), fNo, spot.SpotId())
}

func checkoutHandler() {
	vehicleId := enterVehicleNo()
	spot, ok := vehicleSpot[vehicleId]
	if !ok {
		fmt.Println("No vehicle found")
		return
	}
	veh := spot.GetParkedVehicle()
	spot.UnParkVehicle()
	fmt.Printf("Successfully checkout %v, spotId: %v\n", veh.GetId(), spot.SpotId())
}

func displayFloor() {
	f := chooseFloor()
	if f != nil {
		f.Display()
	}
}

// helper
func chooseOptions() int {
	var op int
	fmt.Println("===========================")
	fmt.Println(`
Choose options ->
1. To CheckIn
2. To CheckOut
3. Display floor
		`)
	fmt.Scan(&op)
	return op
}

func chooseFloor() floor.IFloor {
	var sno int
	op := ""
	for i := range floorList {
		op += fmt.Sprintf("%v: %v Floor\n", i, i)
	}

	fmt.Printf(`
Choose floor No:
-1. exit
%v
`, op)
	fmt.Scan(&sno)
	if sno == -1 {
		return nil
	}
	if sno >= 0 && sno < len(floorList) {
		return floorList[sno]
	}
	return chooseFloor()
}

func chooseVehicle() int {
	var sno int
	op := ""
	for i, v := range vehicle.GetAllSupportedVehicleName() {
		op += fmt.Sprintf("%v: %v Vehicle\n", i, v)
	}

	fmt.Printf(`
Choose Vehicle:
-1. exit
%v
`, op)
	fmt.Scan(&sno)
	if sno == -1 {
		return -1
	}
	if sno < 0 || sno >= len(vehicle.GetAllSupportedVehicleName()) {
		return chooseVehicle()
	}
	return sno
}

func enterVehicleNo() (vehicleId string) {
	fmt.Printf(`
Enter Vehicle No: 	
`)
	fmt.Scanf("%s", &vehicleId)
	return
}
