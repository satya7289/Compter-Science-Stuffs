package vehicle

import (
	"fmt"
	"time"
)

type PName string

const (
	A PName = "A"
	B PName = "B"
)

type Iprice interface {
	Calculate(time.Duration) float64
}

func NewPrice(n PName) Iprice {
	switch n {
	case A:
		return newAprice()
	case B:
		return newBprice()
	default:
		panic(fmt.Sprintf("unsupported implemented %v", n))
	}
}

// Aprice
type APrice struct {
	rate []rateT
}

func newAprice() *APrice {
	return &APrice{
		rate: []rateT{
			{
				dur:   time.Hour,
				price: 50,
			},
			{
				dur:   2 * time.Hour,
				price: 30,
			},
			{
				infinte: true,
				price:   10,
			},
		},
	}
}

func (r APrice) Calculate(d time.Duration) float64 {
	return calculateHelper(d, r.rate, 0)
}

// Bprice
type BPrice struct {
	rate []rateT
}

func (r BPrice) Calculate(d time.Duration) float64 {
	return calculateHelper(d, r.rate, 0)
}

func newBprice() *BPrice {
	return &BPrice{
		rate: []rateT{
			{
				dur:   time.Hour,
				price: 30,
			},
			{
				dur:   2 * time.Hour,
				price: 10,
			},
			{
				infinte: true,
				price:   5,
			},
		},
	}
}

type rateT struct {
	dur     time.Duration
	price   float64
	infinte bool
}

func calculateHelper(d time.Duration, r []rateT, i int) float64 {
	if i == len(r) || d <= 0 {
		return 0
	}
	if r[i].infinte {
		return r[i].price
	}
	return r[i].price + calculateHelper(d-r[i].dur, r, i+1)
}
