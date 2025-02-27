package logger

import "fmt"

type warn struct {
	next  ILogger
	level LogLevel
}

func newWarn(l LogLevel) ILogger {
	return &warn{level: l, next: newError(l)}
}

func (l *warn) Log(level LogLevel, data ...interface{}) {
	if level == WARN {
		fmt.Println("WARN", data)
	} else if l.level < level {
		l.next.Log(level, data...)
	}
	// if level != WARN {
	// 	l.next.Log(level, data...)
	// } else if l.level >= WARN && level == WARN {
	// 	fmt.Println("WARN", data)
	// }
}
