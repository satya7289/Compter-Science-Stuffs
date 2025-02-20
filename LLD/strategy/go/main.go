package main

import (
	"fmt"
	"strategy/pkg/drive"
	"strategy/pkg/vehicle"
)

func main() {
	fmt.Println("Strategy Pattern")

	fast := drive.NewDrive("fast")
	slow := drive.NewDrive("slow")

	car := vehicle.NewVehicle("car", fast)
	bike := vehicle.NewVehicle("bike", slow)

	car.Drive()
	bike.Drive()
	fmt.Println("car no of wheel: ", car.NoOfWheel())
	fmt.Println("bike no of wheel: ", bike.NoOfWheel())
}
