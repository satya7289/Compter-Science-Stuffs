package parking

import (
	"fmt"
	"parkingalot/pkg/floor"
	"parkingalot/pkg/payment"
	"parkingalot/pkg/vehicle"
	"time"
)

var handler = map[int]func(){
	1: checkInHandler,
	2: checkoutHandler,
	3: displayFloor,
	4: listTransaction,
}

var (
	floorList      []floor.IFloor
	vehiclePricing map[vehicle.VehicleName]vehicle.Iprice
)

func InitParkinglot() {
	floorList = append(floorList, floor.NewFloor(0, 3, map[floor.SpotName]int{floor.Small: 10, floor.Large: 5, floor.Electric: 2}))
	floorList = append(floorList, floor.NewFloor(1, 3, map[floor.SpotName]int{floor.Small: 10, floor.Large: 5, floor.Electric: 2}))

	vehiclePricing = make(map[vehicle.VehicleName]vehicle.Iprice)
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
	var floor floor.IFloor
	for i, f := range floorList {
		fNo = i
		floor = f
		if spot, ok = f.AvaliableSpot(); ok {
			fmt.Println("Available Parking for ", newVeh)
			break
		}
	}
	if !ok {
		fmt.Println("Parking not available for ", newVeh)
		return
	}

	AddNewTransaction(NewTransaction(nil, floor, spot, newVeh))
	spot.ParkVehicle(newVeh)
	fmt.Printf("Successfully %v:%v parked on floor: %v, spotId: %v\n", newVeh, newVeh.GetId(), fNo, spot.SpotId())
}

func checkoutHandler() {
	vehicleId := enterVehicleNo()
	transaction := FindTransactionByVehicleId(vehicleId)
	if transaction == nil {
		fmt.Println("No vehicle found")
		return
	}

	veh := transaction.Spot.GetParkedVehicle()
	pricing, ok := vehiclePricing[veh.GetVehicleName()]
	if !ok {
		panic("pricing not found")
	}
	exitTime := time.Now()
	totalDuration := exitTime.Sub(veh.GetEntryTime())
	priceToPay := pricing.Calculate(time.Since(veh.GetEntryTime()))
	fmt.Printf("Total duration: %v, Total pay amount: %v\n", totalDuration, priceToPay)

	payment := choosePayment()
	transaction.Spot.UnParkVehicle()
	transaction.CompleteTransaction(nil, payment)
	fmt.Printf("Successfully checkout %v, spotId: %v\n", veh.GetId(), transaction.Spot.SpotId())
}

func displayFloor() {
	f := chooseFloor()
	if f != nil {
		f.Display()
	}
}

func listTransaction() {
	fmt.Println("All transactions:")
	PrintAllTransactions()
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
4. List transactions
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

func choosePayment() payment.IPayment {
	var paymentMethod int
	fmt.Printf(`
Choose Payment Method:
1: Cash
2: Online
`)
	fmt.Scan(&paymentMethod)
	switch paymentMethod {
	case 1:
		return payment.NewPayment(payment.Cash)
	case 2:
		return payment.NewPayment(payment.Online)
	}
	return choosePayment()
}

func enterVehicleNo() (vehicleId string) {
	fmt.Printf(`
Enter Vehicle No: 	
`)
	fmt.Scanf("%s", &vehicleId)
	return
}
