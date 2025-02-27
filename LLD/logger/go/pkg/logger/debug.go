package logger

import "fmt"

type debug struct {
	next  ILogger
	level LogLevel
}

func newDebug(l LogLevel) ILogger {
	return &debug{level: l, next: newInfo(l)}
}

func (l *debug) Log(level LogLevel, data ...interface{}) {
	if level == DEBUG {
		fmt.Println("DEBUG", data)
	} else if l.level < level {
		l.next.Log(level, data)
	}
}
