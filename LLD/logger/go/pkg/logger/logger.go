package logger

type LogLevel int

const (
	DEBUG LogLevel = iota - 1
	INFO
	WARN
	ERROR
	FETAL
)

func (l LogLevel) Valid() bool {
	if l < -1 && l > 3 {
		return false
	}
	return true
}

type ILogger interface {
	Log(LogLevel, ...interface{})
}

func NewLogger(l LogLevel) ILogger {
	return &logger{
		level: l,
		next:  newDebug(l),
	}
}

type logger struct {
	next  ILogger
	level LogLevel
}

func (l *logger) Log(level LogLevel, data ...interface{}) {
	if !level.Valid() {
		panic("invalid log level")
	}
	l.next.Log(level, data...)
}
