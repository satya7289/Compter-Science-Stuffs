package logger

import "fmt"

type info struct {
	next  ILogger
	level LogLevel
}

func newInfo(l LogLevel) ILogger {
	return &info{level: l, next: newWarn(l)}
}

func (l *info) Log(level LogLevel, data ...interface{}) {
	if level == INFO {
		fmt.Println("INFO", data)
	} else if l.level < level {
		l.next.Log(level, data...)
	}
}
