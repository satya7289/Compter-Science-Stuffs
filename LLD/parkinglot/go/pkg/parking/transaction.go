package parking

import (
	"fmt"
	"parkingalot/pkg/floor"
	"parkingalot/pkg/payment"
	"parkingalot/pkg/vehicle"
)

var allTransaction []*Transaction

func init() {
	allTransaction = make([]*Transaction, 0)
}

type Transaction struct {
	Spot    floor.Ispot
	Floor   floor.IFloor
	Vehicle vehicle.IVehicle

	EntryGate floor.IDoor
	ExitGate  floor.IDoor

	Payment payment.IPayment
}

func NewTransaction(entryGate floor.IDoor, floor floor.IFloor, spot floor.Ispot, veh vehicle.IVehicle) *Transaction {
	return &Transaction{
		EntryGate: entryGate,
		Spot:      spot,
		Floor:     floor,
		Vehicle:   veh,
	}
}

func (t *Transaction) CompleteTransaction(exitgate floor.IDoor, pay payment.IPayment) {
	t.ExitGate = exitgate
	t.Payment = pay
}

func PrintAllTransactions() {
	for _, t := range allTransaction {
		fmt.Printf(`
Vehicle: %v
Entry Gate: %v, Entry Time: %v
Floor: %v, Spot: %v
Payment: %v,
Exit Time: %v, Exit Gate: %v
`, t.Vehicle.GetId(), t.EntryGate, t.Vehicle.GetEntryTime(), t.Floor.GetFloorNo(), t.Spot.SpotId(), t.Payment, t.Vehicle.GetExitTime(), t.ExitGate)
	}
	fmt.Println()
}

func AddNewTransaction(t *Transaction) {
	allTransaction = append(allTransaction, t)
}

func FindTransactionByVehicleId(vehicleId string) *Transaction {
	for _, v := range allTransaction {
		if v.Vehicle != nil && v.Vehicle.GetId() == vehicleId {
			return v
		}
	}
	return nil
}
