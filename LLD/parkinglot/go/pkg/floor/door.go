package floor

type DoorType string

const (
	Entry DoorType = "entry"
	Exit  DoorType = "exit"
)

type IDoor interface {
	door()
}

func NewDoor(n DoorType) IDoor {
	switch n {
	case Entry:
		return &EntryDoor{}
	case Exit:
		return &ExitDoor{}
	default:
		panic("unknown door type")
	}
}

// entry door
type EntryDoor struct{}

func (e *EntryDoor) door() {}

// exit door
type ExitDoor struct{}

func (e *ExitDoor) door() {}
