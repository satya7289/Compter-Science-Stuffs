package observe

import "fmt"

type EmailObserver struct {
}

func (p *EmailObserver) Listen(o IObservable) {
	fmt.Println("email send for ", o)
}

func newEmailObserver() *EmailObserver {
	return &EmailObserver{}
}
