package observe

import "fmt"

type PhoneObservable struct {
	stock int
	list  []IObserver
}

func (p *PhoneObservable) Notify() {
	for _, v := range p.list {
		v.Listen(p)
	}
}

func (p *PhoneObservable) AddObserve(o IObserver) {
	p.list = append(p.list, o)
}

func (p *PhoneObservable) UpdateData(data interface{}) {
	s, _ := data.(int)
	p.stock = s
	if p.stock > 0 {
		p.Notify()
	}
}

func (p *PhoneObservable) GetData() interface{} {
	return p.stock
}

func (p *PhoneObservable) String() string {
	return fmt.Sprintf("phone %v", p.stock)
}
