package main

import (
	"fmt"
	"observer/pkg/observe"
)

func main() {
	fmt.Println("Observer pattern")

	email := observe.NewObserver("email")
	sms := observe.NewObserver("sms")

	phone := observe.NewObservable("phone")
	phone.AddObserve(email)
	phone.AddObserve(sms)

	laptop := observe.NewObservable("laptop")
	laptop.AddObserve(email)
	laptop.AddObserve(sms)

	phone.UpdateData(0)
	laptop.UpdateData(0)
	fmt.Println("should not notify observers")

	phone.UpdateData(2)
	laptop.UpdateData(2)
	fmt.Println("should notify observers")

}
