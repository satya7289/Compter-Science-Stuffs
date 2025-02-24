package payment

import "fmt"

type PaymentName string

var (
	Cash   PaymentName = "cash"
	Online PaymentName = "online"
)

type IPayment interface {
	Pay()
}

func NewPayment(n PaymentName) IPayment {
	switch n {
	case Cash:
		return &CashPayment{}
	case Online:
		return &OnlinePayment{}
	default:
		panic("unknown payment method")
	}
}

type CashPayment struct{}

func (c *CashPayment) Pay() {
	fmt.Println("payment done")
}
func (c *CashPayment) String() string { return string(Cash) }

type OnlinePayment struct{}

func (c *OnlinePayment) Pay() {
	fmt.Println("payment done")
}
func (c *OnlinePayment) String() string { return string(Online) }
