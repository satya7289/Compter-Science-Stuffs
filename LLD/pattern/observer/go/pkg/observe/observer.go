package observe

type IObserver interface {
	Listen(IObservable)
}

func NewObserver(name string) IObserver {
	switch name {
	case "sms":
		return newSMSObserver()
	case "email":
		return newEmailObserver()
	default:
		panic("not implemented name")
	}
}
