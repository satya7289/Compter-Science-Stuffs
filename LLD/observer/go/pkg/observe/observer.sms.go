package observe

import "fmt"

type SMSObserver struct {
}

func (p *SMSObserver) Listen(o IObservable) {
	fmt.Println("sms send for", o)
}

func newSMSObserver() *SMSObserver {
	return &SMSObserver{}
}
