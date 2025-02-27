package logger

import "fmt"

type error struct {
	next  ILogger
	level LogLevel
}

func newError(l LogLevel) ILogger {
	return &error{level: l, next: newFetal(l)}
}

func (l *error) Log(level LogLevel, data ...interface{}) {
	if level == ERROR {
		fmt.Println("ERROR", data)
	} else if l.level < level {
		l.next.Log(level, data...)
	}
}
