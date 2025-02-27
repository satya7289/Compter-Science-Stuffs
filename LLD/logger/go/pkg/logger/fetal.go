package logger

import "fmt"

type fetal struct {
	level LogLevel
}

func newFetal(l LogLevel) ILogger {
	return &fetal{level: l}
}

func (l *fetal) Log(level LogLevel, data ...interface{}) {
	if level == FETAL {
		fmt.Println("FETAL", data)
	}
}
