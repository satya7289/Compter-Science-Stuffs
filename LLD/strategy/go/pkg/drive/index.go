package drive

type IDrive interface {
	Drive()
}

func NewDrive(name string) IDrive {
	switch name {
	case "fast":
		return &FastDrive{}
	case "slow":
		return &SlowDrive{}
	default:
		panic("unsupported drive")
	}
}
