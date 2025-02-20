package observe

import "fmt"

type LaptopObservable struct {
	stock int
	list  []IObserver
}

func (p *LaptopObservable) Notify() {
	for _, v := range p.list {
		v.Listen(p)
	}
}

func (p *LaptopObservable) AddObserve(o IObserver) {
	p.list = append(p.list, o)
}

func (p *LaptopObservable) UpdateData(data interface{}) {
	s, _ := data.(int)
	p.stock = s
	if p.stock > 0 {
		p.Notify()
	}
}

func (p *LaptopObservable) GetData() interface{} {
	return p.stock
}

func (p *LaptopObservable) String() string {
	return fmt.Sprintf("laptop %v", p.stock)
}
