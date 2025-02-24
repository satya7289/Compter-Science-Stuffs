package observe

type IObservable interface {
	GetData() interface{}
	UpdateData(interface{})
	AddObserve(IObserver)
	Notify()
}

func NewObservable(name string) IObservable {
	switch name {
	case "phone":
		return &PhoneObservable{}
	case "laptop":
		return &LaptopObservable{}
	default:
		panic("unsupported name: " + name)
	}
}
